
import pyttsx3
import threading



def speak_alert(text):
    """Runs TTS in a separate thread so it doesnt block the server"""
    def _speak():
        local_engine = pyttsx3.init() # Re-init for thread safety
        local_engine.say(text)
        local_engine.runAndWait()
    
    threading.Thread(target=_speak).start()
