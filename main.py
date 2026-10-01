
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import os
import webbrowser
import subprocess


# ==========================================
# NOVA VOICE ENGINE
# ==========================================

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Nova:", text)
    engine.say(text)
    engine.runAndWait()


# ==========================================
# LISTEN FUNCTION
# ==========================================

def listen(duration=5):

    recognizer = sr.Recognizer()
    sample_rate = 16000

    print("\n🎤 Nova is listening...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    temp_file.close()

    wav.write(
        temp_file.name,
        sample_rate,
        recording
    )

    try:

        with sr.AudioFile(temp_file.name) as source:
            audio = recognizer.record(source)

        print("🔎 Understanding...")

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:

        print("Nova: I couldn't understand you.")

        return ""

    except sr.RequestError:

        print("Nova: Speech recognition service is unavailable.")

        return ""

    finally:

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)


# ==========================================
# COMMAND HANDLER
# ==========================================

def handle_command(command):

    # --------------------------------------
    # YOUTUBE
    # --------------------------------------

    if "youtube" in command:

        speak("Opening YouTube.")

        webbrowser.open("https://www.youtube.com")


    # --------------------------------------
    # GOOGLE
    # --------------------------------------

    elif "google" in command:

        speak("Opening Google.")

        webbrowser.open("https://www.google.com")


    # --------------------------------------
    # GMAIL
    # --------------------------------------

    elif "gmail" in command:

        speak("Opening Gmail.")

        webbrowser.open("https://mail.google.com")


    # --------------------------------------
    # NOTEPAD
    # --------------------------------------

    elif "notepad" in command:

        speak("Opening Notepad.")

        subprocess.Popen("notepad.exe")


    # --------------------------------------
    # CALCULATOR
    # --------------------------------------

    elif "calculator" in command or "calculate" in command:

        speak("Opening Calculator.")

        subprocess.Popen("calc.exe")


    # --------------------------------------
    # FILE EXPLORER
    # --------------------------------------

    elif "file explorer" in command or "files" in command:

        speak("Opening File Explorer.")

        subprocess.Popen("explorer.exe")


    # --------------------------------------
    # EXIT
    # --------------------------------------

    elif (
        "exit" in command
        or "goodbye" in command
        or "stop" in command
        or "shutdown" in command
    ):

        speak("Goodbye Priya. See you later!")

        return False


    # --------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------

    else:

        speak("Sorry, I don't know that command yet.")


    return True


# ==========================================
# MAIN NOVA LOOP
# ==========================================

speak("Hello Priya. I am Nova.")

running = True

while running:

    # Listen for wake word
    command = listen()

    if not command:
        continue


    # ======================================
    # WAKE WORD: HEY NOVA
    # ======================================

    if "hey nova" in command:

        # ----------------------------------
        # STOP NOVA
        # ----------------------------------

        if (
            "stop" in command
            or "exit" in command
            or "goodbye" in command
            or "shutdown" in command
        ):

            speak("Okay Priya, shutting down.")

            running = False

            break


        # ----------------------------------
        # NOVA ACTIVATED
        # ----------------------------------

        speak("Yes Priya, I'm listening.")

        # Listen for actual command
        command = listen()

        if command:

            running = handle_command(command)

