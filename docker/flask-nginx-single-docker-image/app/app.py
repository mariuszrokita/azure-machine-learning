import datetime

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from Flask in a container, {datetime.datetime.utcnow().isoformat()}"

if __name__ == "__main__":  
    app.run(debug=True, host='0.0.0.0', use_reloader=False)