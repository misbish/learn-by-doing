from flask import Flask

app = Flask(__name__)

@app.route("/")
def display_hello_world():
    return "HELLO WOLRD"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)