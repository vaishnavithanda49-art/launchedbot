# 🤖 AutoClone AI – Intelligent Virtual Meeting Assistant

<p align="center">

**An AI-powered virtual meeting assistant that listens, transcribes, summarizes, and manages meeting conversations in real time.**

</p>

---

## 📖 Overview

AutoClone AI is an intelligent meeting assistant designed to simplify online meetings by automatically capturing conversations, generating accurate transcripts, identifying important discussion points, and creating concise meeting summaries.

The system leverages Artificial Intelligence, Speech Recognition, and Natural Language Processing (NLP) to help users focus on discussions instead of taking manual notes. It is suitable for business meetings, online classes, interviews, webinars, and collaborative sessions.

---

## ✨ Features

* 🎤 Real-time speech recognition
* 📝 Automatic meeting transcription
* 📄 AI-generated meeting summaries
* 🔍 Keyword detection and intelligent responses
* 💾 Automatic transcript and summary storage
* 📂 Meeting history management
* 🌐 Web-based user interface
* 🔊 Text-to-Speech (AI voice responses)
* 📁 Upload and process recorded meeting audio
* 📊 Meeting logs and analytics

---

## 🚀 Upcoming Features

* 👥 Speaker Identification (Speaker Diarization)
* 😊 Emotion & Sentiment Analysis
* 🌍 Multi-language Transcription
* 📅 Calendar Integration
* 📧 Automatic Email Summaries
* 🤖 AI Chat with Previous Meetings
* 📌 Action Item & Deadline Extraction
* 📄 PDF Meeting Report Generation
* ☁️ Cloud Storage Support
* 🎥 Zoom & Google Meet Integration

---

## 🛠️ Technologies Used

### Programming Language

* Python 3.10

### Backend

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite
* Supabase (Authentication & Cloud Services)

### Artificial Intelligence

* OpenAI Whisper
* Google Speech Recognition
* Hugging Face Transformers
* PyTorch

### Speech Processing

* SpeechRecognition
* PyAudio
* gTTS (Google Text-to-Speech)
* playsound

### Speaker Recognition

* Pyannote Audio *(In Progress)*

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
AutoCloneAI/
│
├── app.py
├── advtranscript.py
├── database.db
├── meeting.log
├── meeting_transcript.txt
│
├── static/
│
├── templates/
│
├── uploads/
│
└── audio_logs/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vaishnavithanda49-art/ai-meeting-assistant.git
```

### 2. Navigate to the Project

```bash
cd ai-meeting-assistant
```

### 3. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🔄 Workflow

```text
User Speech
      │
      ▼
Speech Recognition
      │
      ▼
Speech-to-Text Conversion
      │
      ▼
AI Processing
      │
 ┌────┴─────────────┐
 │                  │
 ▼                  ▼
Transcript      AI Summary
 │                  │
 └──────┬───────────┘
        ▼
 Database Storage
        │
        ▼
 History Dashboard
```

---

## 🎯 Applications

* Corporate Meetings
* Online Classes
* Team Collaboration
* Project Discussions
* Interview Recording
* Webinars
* Personal Note Taking

---

## 🔮 Future Scope

AutoClone AI aims to become a complete AI-powered meeting companion capable of joining online meetings automatically, recognizing individual speakers, understanding conversation context, extracting action items, generating professional meeting minutes, and enabling users to interact with previous meetings using conversational AI.

---

## 👥 Contributors

| Name | Role |
|------|------|
| **Vaishnavi Thanda** | Backend Development, AI Integration, Speech Recognition |
| **Kundana Garikapati** | Frontend Development, UI Design, Database Integration |
---

## 📄 License

This project is intended for educational, research, and demonstration purposes.

---

## ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star** on GitHub. Your support helps improve the project and encourages future development.
