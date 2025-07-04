# VYBINTZ – AI-Powered Nightlife Assistant
from flask import Flask, render_template, jsonify
import cv2
import numpy as np
import pandas as pd
import mediapipe as mp
import random
import datetime
import os

app = Flask(__name__)

# DataFrame to collect analysis results during runtime
history = pd.DataFrame(columns=[
    "timestamp",
    "headcount",
    "spend_rate",
    "sentiment_score",
    "mood",
])

# Simulated function: Detects crowd size and returns estimated headcount

def get_head_count(frame):
    """Return a simulated crowd size after basic image processing."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _ = cv2.GaussianBlur(gray, (5, 5), 0)
    return int(np.random.randint(20, 100))

# Simulated function: Analyzes energy level based on noise level or movement

def analyze_vibe(frame):
    """Simulate vibe analysis using MediaPipe."""
    with mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5):
        vibe_score = np.random.uniform(0.0, 1.0)
    if vibe_score > 0.75:
        return "High energy – switch to party mode."
    elif vibe_score > 0.4:
        return "Moderate vibe – keep it flowing."
    else:
        return "Low energy – drop a banger."

# Simulated function: Tracks spending rates and emotional sentiment

def analyze_financial_and_sentiment():
    spend_rate = random.uniform(100, 1000)  # Dummy spend rate
    sentiment_score = random.uniform(0.0, 1.0)  # Dummy sentiment score
    if sentiment_score < 0.3:
        notification = "Alert: Negative sentiment detected. Staff attention required."
    else:
        notification = "Positive vibe detected."
    return spend_rate, sentiment_score, notification

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Display the most recent vibe checks in a table."""
    table_html = history.tail(20).to_html(classes="table", index=False)
    return render_template('dashboard.html', table=table_html)

@app.route('/affiliate')
def affiliate():
    return render_template('affiliate.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Use a blank frame to simulate camera input
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    count = get_head_count(dummy_frame)
    mood = analyze_vibe(dummy_frame)
    spend, sentiment, alert = analyze_financial_and_sentiment()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "timestamp": timestamp,
        "headcount": count,
        "spend_rate": spend,
        "sentiment_score": sentiment,
        "mood": mood,
    }
    global history
    history = pd.concat([history, pd.DataFrame([entry])], ignore_index=True)

    result = entry.copy()
    result.update({"notification": alert})
    result["spend_rate"] = round(result["spend_rate"], 2)
    result["sentiment_score"] = round(result["sentiment_score"], 2)
    return jsonify(result)

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    debug = os.getenv('FLASK_DEBUG', '1') in ('1', 'true', 'True')
    app.run(host=host, port=port, debug=debug)
