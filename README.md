# 🔍 Realtime Log Viewer (Flask + SSE)

This project is a simple real-time log monitoring web app built with **Flask** and **Server-Sent Events (SSE)**. It mimics the behavior of the `tail -f` command on a remote log file, allowing users to watch live updates to the log file directly in their browser.

---

## 🧠 Problem Statement

You need to build a solution that:

- Runs a **server-side program** monitoring an append-only log file (potentially very large).
- Streams updates to **multiple web clients** in real time.
- When a client connects, it shows the **last 10 lines** of the log.
- Clients see new lines **automatically without refreshing or reloading** the page.
- The server sends **only the new lines** added to the file, not the entire file.
- No external tail libraries or tools can be used; the functionality must be implemented from scratch.

---

## 🚀 Features

- Real-time streaming of log updates over HTTP using SSE.
- Efficient reading of the last 10 lines of potentially large files.
- Multiple clients supported simultaneously.
- Auto-scrolls log output in the browser.
- Clean, simple UI with monospace font for easy log reading.

---

## 📁 Project Structure

realtime-log-streamer/
├── app.py
├── test.log
└── templates/
    └── log_viewer.html


---

## ⚙️ Setup Instructions

1. **Clone this repository:**

git clone https://github.com/Harshul26Nanwani/realtime-log-viewer.git
cd realtime-log-viewer

2. (Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux


3. Install dependencies:
   
pip install flask

4. Create a log file:

echo Starting log > test.log


5. Run the Server:
   
    python3.13 app.py

6. Open in browser:

   http://localhost:5000/log



🧪 Simulate Log Updates
In a separate terminal:

echo New log line >> test.log

You’ll see updates appear live in the browser.

   





