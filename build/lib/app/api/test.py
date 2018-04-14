from app import app

@app.route('/summarize/<data>', methods=["GET"])
def summarize(data):
    return data
