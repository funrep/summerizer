from app import app
from flask import request

@app.route('/summarize/', methods=["POST"])
def summarize():
    return request.data
