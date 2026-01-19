
import pyttsx3
import threading
import random
from data.roasts import ROASTS
from data.praises import PRAISES


def speak_alert(speak_type):
    
    def _speak():
        try:
            if speak_type == "roast":
                phrase = random.choice(ROASTS)
            else:
                phrase = random.choice(PRAISES)
            print(f"💀 SPEAKING: {phrase}")
            engine = pyttsx3.init()
            engine.setProperty('rate', 160)
            engine.say(phrase)
            engine.runAndWait()
        except:
            pass
    threading.Thread(target=_speak).start()