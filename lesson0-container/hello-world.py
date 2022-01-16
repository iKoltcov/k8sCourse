from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = "<h1>Hello, World!</h1>"
    response = f"{response}<br><br>environment variables:"
    for k, v in os.environ.items():
        response = f'{response}<br>{k}={v}'
    return response

if __name__ == "__main__":
    host = str(os.environ.get("HOST", "0.0.0.0"))
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True, host=host, port=port)