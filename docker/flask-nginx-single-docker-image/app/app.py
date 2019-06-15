from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():  
  return "Hello from Flask in a container"

if __name__ == "__main__":  
    app.run(debug=True, host='0.0.0.0', use_reloader=False)