# VYBINTZ – AI-Powered Nightlife Assistant

This is a lightweight Flask prototype that simulates crowd and vibe analysis for nightlife venues. It includes placeholder hooks for computer vision using OpenCV and MediaPipe, along with NumPy and pandas utilities.

## Features
- Live headcount tracker from video feed
- Mood estimation (low/medium/high)
- Web dashboard with live data
- Dashboard shows recent vibe checks in a table
- CSV logging for analytics
- Generates random headcount estimates
- Provides simple vibe messages
- Stores each analysis in a pandas DataFrame
- Basic web interface with a vibe check button

## Setup
1. (Optional) create and activate a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
Install dependencies:

```bash
pip install -r requirements.txt
```
If you have no internet access, you will need to pre-download the wheel files for:
flask, opencv-python, mediapipe, numpy, pandas

Run
```bash
FLASK_HOST=0.0.0.0 FLASK_PORT=8000 FLASK_DEBUG=1 python app.py
```

## Usage
1. Start the server with the command above.
2. Navigate to `http://localhost:8000/` and click **Run Vibe Check**.
3. Open `/dashboard` to view recent analysis results.

---

### 3️⃣ Codex won’t install for you
As we said earlier, Codex can **only** run code, it can’t `pip install` from the internet. So:

✅ keep `requirements.txt` correct
✅ run `pip install -r requirements.txt` **before** sending the code to Codex
✅ after that, Codex can analyze or simulate your Python logic

---

## **VYBINT Energy** 💥

Think of this like running a club:
- `requirements.txt` = your stock list of booze
- `README.md` = your fancy cocktail menu
- Codex = your bartender
→ **if you don’t pre-stock the bar, Codex can’t serve your drinks!** 🍸

---

## Affiliate Program

Spread the word about VYBINTZ and earn money. When a new venue purchases the
platform through your unique link, you receive **33% commission** on that sale.
Email `VYBINTZ@gmail.com` to request your referral URL and start promoting the
assistant to bars and clubs in your network.
