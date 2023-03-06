

from flask import Flask, request, Response
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/webhook', methods=['POST'])
def return_response():
    print(request.json)
    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3600, debug=True, threaded=True)
