from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import random
import time
import threading

app = Flask(__name__)

REQUESTS = Counter("demo_requests_total", "Total demo requests")
IN_PROGRESS = Gauge("demo_inprogress_requests", "In-progress demo requests")
RND_GAUGE = Gauge("demo_random_value", "Random gauge for demo")

@app.route("/")
def index():
    REQUESTS.inc()
    IN_PROGRESS.inc()

    time.sleep(random.uniform(0.05, 0.3))
    IN_PROGRESS.dec()

    RND_GAUGE.set(random.random() * 100)
    return "Hello from demo app\n"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
