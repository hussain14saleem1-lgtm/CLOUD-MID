from flask import Flask, render_template, request, redirect, url_for
import redis
import os

app = Flask(__name__)

# Connect to Redis using the service name from docker-compose
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/', methods=['GET'])
def index():
    # Increment visit counter on every page load
    visits = r.incr('visits')
    return render_template('index.html', visits=visits)

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form.get('message', '').strip()
    if message:
        r.rpush('messages', message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)