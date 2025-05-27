from flask import Flask, Response, render_template
import os
import time
import threading

app = Flask(__name__)

LOG_FILE = "test.log"
clients = []

# Efficient function to get last N lines of large file
def tail(file_path, lines=10):
    with open(file_path, 'rb') as f:
        f.seek(0, os.SEEK_END)
        end = f.tell()
        block_size = 1024
        data = b''
        while lines > 0 and end > 0:
            read_size = min(block_size, end)
            f.seek(end - read_size, os.SEEK_SET)
            data = f.read(read_size) + data
            lines -= data.count(b'\n')
            end -= read_size
        return b"\n".join(data.splitlines()[-10:]).decode(errors='ignore')

# Background thread to watch for new log lines
def log_monitor():
    with open(LOG_FILE, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            for client in clients[:]:
                try:
                    client.put(line)
                except:
                    clients.remove(client)

@app.route("/log")
def log_page():
    return render_template("log_viewer.html")

@app.route("/stream")
def stream():
    def event_stream():
        from queue import Queue
        q = Queue()
        clients.append(q)

        # Send last 10 lines on connect
        initial = tail(LOG_FILE)
        for line in initial.splitlines():
            yield f"data: {line}\n\n"

        while True:
            result = q.get()
            yield f"data: {result.strip()}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    threading.Thread(target=log_monitor, daemon=True).start()
    app.run(debug=True, threaded=True)
