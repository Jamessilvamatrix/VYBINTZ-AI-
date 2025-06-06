# VYBINTZ – AI-Powered Nightlife Assistant
from flask import Flask, render_template, jsonify
import cv2
import numpy as np
import datetime

app = Flask(__name__)

# Simulated function: Detects crowd size and returns estimated headcount

def get_head_count(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Simulated detection logic (replace with actual AI model)
    people_count = np.random.randint(20, 100)  # Dummy headcount
    return people_count

# Simulated function: Analyzes energy level based on noise level or movement

def analyze_vibe(frame):
    vibe_score = np.random.uniform(0.0, 1.0)
    if vibe_score > 0.75:
        return "High energy – switch to party mode."
    elif vibe_score > 0.4:
        return "Moderate vibe – keep it flowing."
    else:
        return "Low energy – drop a banger."

# Simulated function: Tracks spending rates and emotional sentiment

def analyze_financial_and_sentiment():
    spend_rate = np.random.uniform(100, 1000)  # Dummy spend rate
    sentiment_score = np.random.uniform(0.0, 1.0)  # Dummy sentiment score
    if sentiment_score < 0.3:
        notification = "Alert: Negative sentiment detected. Staff attention required."
    else:
        notification = "Positive vibe detected."
    return spend_rate, sentiment_score, notification

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Simulate receiving a frame (in real app, use camera input)
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    count = get_head_count(dummy_frame)
    mood = analyze_vibe(dummy_frame)
    spend, sentiment, alert = analyze_financial_and_sentiment()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        'headcount': count,
        'mood': mood,
        'spend_rate': round(spend, 2),
        'sentiment_score': round(sentiment, 2),
        'notification': alert,
        'timestamp': timestamp
    })

if __name__ == '__main__':
    app.run(debug=True)
