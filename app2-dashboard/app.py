from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Connect to the same Redis instance (using service name from docker-compose)
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/', methods=['GET'])
def dashboard():
    # Read total number of messages from the Redis list
    message_count = r.llen('messages')
    
    # Read the visit counter (default to 0 if not set yet)
    visit_count = r.get('visits') or 0
    
    return render_template(
        'index.html',
        message_count=message_count,
        visit_count=visit_count
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)