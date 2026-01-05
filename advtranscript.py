import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime
import whisper
from transformers import pipeline as hf_pipeline
from colorama import Fore, Style, init
import logging

# -------------------------------
# Setup
# -------------------------------
init(autoreset=True)
script_dir = os.path.dirname(os.path.abspath(__file__))
transcript_file = os.path.join(script_dir, "meeting_transcript.txt")
summary_file = os.path.join(script_dir, "meeting_summary.txt")
audio_log_dir = os.path.join(script_dir, "audio_logs")
os.makedirs(audio_log_dir, exist_ok=True)

logging.basicConfig(filename=os.path.join(script_dir, "meeting.log"),
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# -------------------------------
# Initialize Whisper + Summarizer
# -------------------------------
print(Fore.CYAN + "🔍 Loading Whisper model (base)...")
whisper_model = whisper.load_model("base")

print(Fore.CYAN + "🧠 Loading AI summarizer...")
summarizer = hf_pipeline("summarization", model="facebook/bart-large-cnn")

# -------------------------------
# Keyword mapping
# -------------------------------
keywords_responses = {
    "note": "I will take a note of that.",
    "deadline": "Got it. I’ll remember this deadline.",
    "project": "Let’s discuss the project details carefully.",
    "action": "Okay, adding this as an action item.",
    "summary": "I’ll prepare a summary of this discussion later.",
    "meeting": "I’m following the meeting discussion.",
    "hello": "Hi there! I’m listening.",
}

# -------------------------------
# Text-to-Speech
# -------------------------------
def speak(text):
    """Speak text aloud using gTTS."""
    print(Fore.GREEN + f"🤖 AI: {text}")
    try:
        filename = os.path.join(script_dir, "temp.mp3")
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(Fore.RED + f"❌ Speech synthesis failed: {e}")

# -------------------------------
# Whisper-based Recognition (Offline)
# -------------------------------
def recognize_with_whisper(audio_data):
    """Transcribe using Whisper offline."""
    temp_audio = os.path.join(audio_log_dir, "temp_audio.wav")
    with open(temp_audio, "wb") as f:
        f.write(audio_data.get_wav_data())

    result = whisper_model.transcribe(temp_audio, fp16=False)
    return result["text"]

# -------------------------------
# Speech Recognition Listener
# -------------------------------
def listen_and_transcribe(recognizer, mic):
    """Capture and transcribe audio from microphone."""
    with mic as source:
        print(Fore.YELLOW + "🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

    # Try Google first, fallback to Whisper
    try:
        print(Fore.CYAN + "🧠 Recognizing via Google API...")
        text = recognizer.recognize_google(audio)
        return text
    except Exception:
        print(Fore.MAGENTA + "⚙️ Google failed, using Whisper (offline)...")
        try:
            return recognize_with_whisper(audio)
        except Exception as e:
            print(Fore.RED + f"❌ Recognition failed: {e}")
            return ""

# -------------------------------
# Keyword responder
# -------------------------------
def respond_if_keyword(text):
    text_lower = text.lower()
    for word, response in keywords_responses.items():
        if word in text_lower:
            speak(response)
            return response
    return None

# -------------------------------
# Summary Generator
# -------------------------------
def generate_summary(transcript):
    if not transcript:
        return "No meeting content recorded."

    full_text = " ".join(transcript)
    ai_summary = summarizer(full_text, max_length=120, min_length=30, do_sample=False)[0]["summary_text"]

    summary = "📄 Meeting Summary\n"
    summary += f"- Total lines captured: {len(transcript)}\n"
    summary += f"- AI Summary: {ai_summary}\n\n"
    summary += "🗒️ Key Points:\n"
    for line in transcript[-5:]:
        summary += "  • " + line + "\n"
    return summary

# -------------------------------
# Main Assistant Loop
# -------------------------------
def main():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.energy_threshold = 400
    recognizer.pause_threshold = 0.8

    mic = sr.Microphone()
    transcript = []

    speak("Hello! I’m ready to listen to your meeting.")

    while True:
        try:
            text = listen_and_transcribe(recognizer, mic)
            if not text.strip():
                print(Fore.LIGHTBLACK_EX + "⚠️ Could not understand. Listening again...")
                continue

            print(Fore.WHITE + f"🗣️ You said: {text}")
            transcript.append(text)
            logging.info(f"You said: {text}")

            # Save live transcript
            with open(transcript_file, "a", encoding="utf-8") as f:
                f.write(text + "\n")

            if "stop meeting" in text.lower():
                speak("Alright, stopping the meeting and preparing your summary.")
                break

            respond_if_keyword(text)

        except sr.WaitTimeoutError:
            print(Fore.LIGHTBLACK_EX + "⌛ No one speaking... waiting.")
        except KeyboardInterrupt:
            print(Fore.RED + "\n🏁 Meeting manually stopped.")
            break

    # Generate and save summary
    print(Fore.CYAN + "\n📝 Generating meeting summary...")
    summary = generate_summary(transcript)
    print(Fore.GREEN + summary)

    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary)

    speak("Meeting summary has been generated and saved successfully.")
    print(Fore.CYAN + f"✅ Summary saved to {summary_file}")
    print(Fore.CYAN + f"✅ Transcript saved to {transcript_file}")


# -------------------------------
# Run
# -------------------------------
if __name__ == "__main__":
    main()
