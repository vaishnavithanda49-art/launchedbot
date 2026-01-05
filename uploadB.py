from flask import Flask, request, jsonify, render_template, redirect, url_for
import whisper, os

app = Flask(__name__)

# Load Whisper model (make sure you installed openai-whisper: pip install openai-whisper)
model = whisper.load_model("base")

# Home route → redirect to upload page
@app.route('/')
def home():
    return redirect(url_for('upload_page'))

# Upload page (renders the HTML form)
@app.route('/upload')
def upload_page():
    return render_template('upload.html')

# Transcription route (handles uploaded audio and returns JSON)
@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        # Check if file is present
        if "audio" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["audio"]

        # Check if filename is empty
        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        # Save file in uploads folder
        os.makedirs("uploads", exist_ok=True)
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        # Run Whisper model
        result = model.transcribe(filepath)
        transcript = result["text"]

        return jsonify({"transcript": transcript})

    except Exception as e:
        # Print error in terminal and return as JSON
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
