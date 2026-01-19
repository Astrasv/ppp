from random import random
import sys
import threading
import time
from flask import Flask, request
import logging

from data.browsers import BROWSER_PROCESS_NAMES
from data.roasts import ROASTS
from app.get_active_windows import ActiveWindows
from roast_modules.roaster_speaker import speak_alert
from roast_modules.log_shame import log_shame
from roast_modules.send_nag import send_nag
from roast_modules.bring_vscode import bring_vscode_to_front


from data.forbidden import FORBIDDEN
from flask import Flask, request
from flask_cors import CORS

import random

app = Flask(__name__)

CORS(app) 

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

ActiveWindowsFetcher = ActiveWindows(sys.platform)

CURRENT_BROWSER_URL = ""
CONSECUTIVE_SECONDS = 0

@app.route('/update', methods=['POST'])
def receive_url():
    global CURRENT_BROWSER_URL
    data = request.json
    url = data.get('url', '')
    
    # Update the global variable
    CURRENT_BROWSER_URL = url
    return "OK", 200


@app.route('/health', methods=['GET'])
def health_check():
    return "Activity Spy is running.", 200

def run_server():
    """Starts the Flask server in a separate thread"""
    app.run(port=5000, use_reloader=False)

def main():
    global CONSECUTIVE_SECONDS
    print("--- 💀 THE DISAPPOINTED SENIOR DEV IS WATCHING 💀 ---")
    threading.Thread(target=run_server, daemon=True).start()

    try:
        while True:
            app_name, window_title = ActiveWindowsFetcher.get_active_windows()
            is_distracted = False
            
            if any(b in app_name for b in ["chrome", "edge", "firefox", "brave"]):
                if any(d in CURRENT_BROWSER_URL for d in FORBIDDEN):
                    is_distracted = True
            
            # --- THE ESCALATION LADDER ---
            if is_distracted:
                CONSECUTIVE_SECONDS += 1
                print(f"Distracted for: {CONSECUTIVE_SECONDS}s")

                # Level 1: Immediate Shame (At 2 seconds)
                if CONSECUTIVE_SECONDS == 2:
                    print("\n!!! DISTRACTION DETECTED !!!")
                    speak_alert("roast") # Speak a roast

                # Level 2: The Nag (At 10 seconds)
                if CONSECUTIVE_SECONDS == 10:
                    send_nag()
                
                # Level 3: Permanent Record (At 20 seconds)
                if CONSECUTIVE_SECONDS == 20:
                    log_shame(CURRENT_BROWSER_URL)
                    speak_alert("roast") # Speak again

                # Level 4: The Force (Every 10s after 30s) -> Force swap window
                if CONSECUTIVE_SECONDS > 30 and CONSECUTIVE_SECONDS % 10 == 0:
                    print("!!! FORCING WINDOW SWAP !!!")
                    bring_vscode_to_front()

            else:
                if CONSECUTIVE_SECONDS > 0:
                    print("-> User returned to work. Timer reset.")
                    speak_alert("praise")
                CONSECUTIVE_SECONDS = 0

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()