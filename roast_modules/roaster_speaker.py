import threading
import random
import os
import ctypes
from gtts import gTTS
from playsound import playsound
from data.roasts import ROASTS
from data.praises import PRAISES

def show_error_popup(text, error_type):
    
    try:
        if error_type == "roast":
            # Critical Error Icon 
            style = 0x10 | 0x1000
            title = "ROAST INCOMING !!!"
        else:
            # Info Icon  for Success
            style = 0x40 | 0x1000 
            title = "GREAT WORK GETTING BACK"

        ctypes.windll.user32.MessageBoxW(0, text, title, style)
    except:
        pass

def play_audio_and_popup(text, speak_type):
    """
    Generates MP3, plays it, and launches the popup simultaneously.
    """
    def _run():
        try:
            print(f"\nSPEAKING: {text}")
            
            filename = f"temp_speech_{random.randint(1000, 9999)}.mp3"
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)

            popup_thread = threading.Thread(target=show_error_popup, args=(text,speak_type), daemon=True)
            popup_thread.start()

            # 3. Play the audio
            playsound(filename)

            os.remove(filename)
            
        except Exception as e:
            print(f"Audio Error: {e}")

    threading.Thread(target=_run).start()

def speak(text, speak_type):
    play_audio_and_popup(text, speak_type)

def speak_alert(speak_type):
    phrase = ""
    if speak_type == "roast":
        phrase = random.choice(ROASTS)
        play_audio_and_popup(phrase, speak_type)
    else:
        phrase = random.choice(PRAISES)
        play_audio_and_popup(phrase, speak_type)

    