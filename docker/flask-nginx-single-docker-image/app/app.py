import datetime

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return f"Hello from Flask in a container, {datetime.datetime.utcnow().isoformat()}"

if __name__ == "__main__":  
    application.run(debug=True, host='0.0.0.0', port=80, use_reloader=False)