from flask import Flask
app = Flask(__name__)

# Simple state management
state = {"next": "Hello"}

@app.route('/')
def hello_world():
    response = state["next"]
    state["next"] = "World" if response == "Hello" else "Hello"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
