# 🤖 Nova Voice Assistant

A simple Python-based voice assistant that listens to the wake word **"Hey Nova"** and performs basic tasks using voice commands.

Nova is designed as a beginner-friendly personal voice assistant project, with plans to gradually add more intelligent features such as AI conversation, system control, web search, and automation.

---

## ✨ Features

Currently, Nova can:

* 🎤 Listen to voice commands
* 🗣️ Respond using text-to-speech
* 👂 Detect the wake word **"Hey Nova"**
* ▶️ Open YouTube
* 🌐 Open Google
* 📧 Open Gmail
* 📝 Open Notepad
* 🧮 Open Calculator
* 📁 Open File Explorer
* 🛑 Stop or exit using voice commands

---

## 🛠️ Technologies Used

* **Python**
* **SpeechRecognition** – Speech-to-text
* **pyttsx3** – Text-to-speech
* **SoundDevice** – Microphone audio recording
* **SciPy** – WAV audio processing
* **Webbrowser** – Opening websites
* **Subprocess** – Controlling Windows applications

---

## 📂 Project Structure

```text
Nova/
│
├── main.py
├── README.md
├── .gitignore
└── venv/
```

> `venv/` is used only for the local Python virtual environment and should not be uploaded to GitHub.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Nova
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
venv\Scripts\Activate.ps1
```

---

## 📦 Install Dependencies

Run:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install sounddevice
pip install numpy
pip install scipy
```

---

## ▶️ Run Nova

Start the assistant using:

```bash
python main.py
```

Nova will say:

> Hello Priya. I am Nova.

Then say:

> **Hey Nova**

Nova will respond:

> **Yes Priya, I'm listening.**

You can then give a command.

---

## 🎙️ Example Commands

| Voice Command      | Action                |
| ------------------ | --------------------- |
| Hey Nova           | Activate Nova         |
| Open YouTube       | Opens YouTube         |
| Open Google        | Opens Google          |
| Open Gmail         | Opens Gmail           |
| Open Notepad       | Opens Windows Notepad |
| Open Calculator    | Opens Calculator      |
| Open File Explorer | Opens File Explorer   |
| Stop               | Stops Nova            |
| Goodbye            | Stops Nova            |
| Exit               | Stops Nova            |

---

## 🔮 Future Improvements

The project will gradually be extended with more advanced features:

* 🧠 AI-powered conversations
* 🔎 Google/web search
* 🎵 Music control
* 📱 Application control
* 💻 Advanced Windows system control
* ⏰ Reminders and alarms
* 📝 Notes and memory
* 🌦️ Weather information
* 📧 Email assistance
* 🔐 User authentication
* 💾 Persistent memory
* 🗣️ More natural conversations
* ⚡ Continuous wake-word detection

---

## 🎯 Project Goal

The main goal of this project is to learn how a voice assistant works by building one from scratch using Python.

Instead of directly using a ready-made assistant, Nova is being developed step-by-step to understand:

**Voice Input → Speech Recognition → Command Processing → Action → Voice Response**

```text
       🎤 User Voice
            │
            ▼
     Speech Recognition
            │
            ▼
       "Hey Nova"
            │
            ▼
      Command Handler
            │
       ┌────┴────┐
       ▼         ▼
    Website    Windows App
       │         │
       └────┬────┘
            ▼
       Nova Response
            │
            ▼
          🔊 Voice
```

---

## 👩‍💻 Author

**Priya Chaudhary**

This project is developed as a personal learning project to explore:

* Python
* Artificial Intelligence
* Speech Recognition
* Automation
* Voice Assistants

---

## 📌 Project Status

🚧 **Currently in Development**

Nova is a continuously evolving project. New features and improvements will be added over time.

---

## ⭐ Future Vision

The long-term goal is to develop Nova into a more capable personal AI assistant that can understand natural language, remember useful information, control applications, search the web, and interact with the computer through voice.

**"Hey Nova, let's build something smart." 🚀**
