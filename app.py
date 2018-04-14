from flask import Flask, Response
from flask import request
from flask import json

app = Flask(__name__)

@app.route("/")
def hello_world():
	return Response("Hello", status=200, mimetype="text/plain")

@app.route('/extract-header')
def extract_header():

	data = json.loads(request.data)
	return data['text'][0:min(len(data['text']), int(data['length']))]

if __name__ == '__main__':
    app.run(debug=True)
