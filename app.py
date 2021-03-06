from flask import Flask, Response
from flask import request
from flask import json
from summarization.markov_chain import markov_chain

app = Flask(__name__)

SUMMARIZER = markov_chain()

@app.route("/")
def hello_world():
    return Response("Hello", status=200, mimetype="text/plain")

@app.route('/extract-header')
def extract_header():
        data = json.loads(request.data)
        return data['text'][0:min(len(data['text']), int(data['length']))]


@app.route("/markov", methods=["POST"])
def summarize():
    data = request.get_data().decode("utf-8")
    SUMMARIZER.learn(data)

    response = SUMMARIZER.generate()

    return Response(response, status=200, mimetype="text/plain")



if __name__ == '__main__':
    app.run(debug=True)
