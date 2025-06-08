import pyttsx3
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


def say(txt):
    if type(txt) is list:
        txt = " ".join(txt)
    engine.say(txt)
    engine.runAndWait()

def search(txt):
    say(txt)

def run_cmd(command):
    command = ' '.join(command)
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        say( f"Error executing command: {e}")


def call_func(func):
    pass