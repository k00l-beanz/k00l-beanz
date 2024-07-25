import pickle
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/hackme", methods=["POST"])
def hackme():
    data = base64.urlsafe_b64decode(request.form["pickled"])
    des = pickle.loads(data)

    return '', 204