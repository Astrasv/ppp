from flask import Flask, request
import logging

from utils.roaster_speaker import speak_alert
from data.forbidden import FORBIDDEN
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app) 

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/update', methods=['POST'])
def receive_url():
    data = request.json
    url = data.get('url', '')
    
    print(f" ==> Active: {url}")

    for keyword in FORBIDDEN:
        if keyword in url:
            print(f"!!! VIOLATION: {keyword} !!!")
            speak_alert("Don't open please")
            
    return "OK", 200

@app.route('/health', methods=['GET'])
def health_check():
    return "Activity Spy is running.", 200


if __name__ == "__main__":

    print("--- Activity Spy Running (CORS Enabled) ---")
    app.run(port=5000)