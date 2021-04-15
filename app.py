from flask import Flask, jsonify 
from flask.globals import request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def home():
    return jsonify(data="Hey")

if __name__ == "__main__":
    app.run()