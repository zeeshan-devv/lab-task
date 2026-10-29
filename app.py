import os
from flask import Flask

app = Flask(__name__)
FILE = "/data/counter.txt"

@app.route("/")
def index():
    os.makedirs("/data", exist_ok=True)
    count = 0
    if os.path.exists(FILE):
        with open(FILE) as f:
            count = int(f.read() or 0)
    count += 1
    with open(FILE, "w") as f:
        f.write(str(count))
    return "Visits: " + str(count) + "\n"
