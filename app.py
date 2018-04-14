from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return Response("Hello", status=200, mimetype="text/plain")

@app.route('/extract-header', methods=["POST"])
def extract_header():
    return request.data[0: min(100, len(request.data))]

if __name__ == '__main__':
    app.run(debug=True)
