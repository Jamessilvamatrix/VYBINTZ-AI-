# VYBINTZ-AI- 
│
├── /backend/
│   ├── headcount_tracker.py
│   ├── mood_analyzer.py
│   ├── video_input.py
│   ├── utils.py
│   └── requirements.txt
│
├── /frontend/
│   ├── app.py
│   ├── templates/
│   │   └── dashboard.html
│   └── static/
│       ├── style.css
│       └── icons/
│
├── /data/
│   └── logs.csv
│
├── README.md
└── LICENSE
headcount_tracker.py
mood_analyzer.py
video_input.py
app.py
dashboard.html
logs.csv
opencv-python
flask
mediapipe
numpy
pandas
# VYBINTZ – AI-Powered Nightlife Assistant

A lightweight prototype for bars and clubs to track crowd size and mood in real time using AI. This MVP is built in Python and Flask with OpenCV and MediaPipe.

## Features
- Live headcount tracker from video feed
- Mood estimation (low/medium/high)
- Web dashboard with live data
- CSV logging for analytics

## Run Locally
```bash
pip install -r requirements.txt
python app.py

---

