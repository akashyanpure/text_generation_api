from flask import Flask, redirect, url_for, render_template,jsonify
from flask.globals import request
from transformers import pipeline
import pickle as pickle
import tensorflow as tf
from pickle import dump

filename = 'finalized_model.sav'
# model = pickle.load(open(filename, 'rb'))
model = tf.keras.models.load_model('saved_models/my_model')
print(model)
if True:
    print("asdf") 
else:
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
    dump(model, open('finalized_model.sav', 'wb'))

app = Flask(__name__,template_folder='../template')

languages = [{'name': 'Javascript'}]
@app.route("/")
def home():
    return jsonify("data")

@app.route("/login",methods = ["POST"])
def login():
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)

# joblib.dump(grid.best_estimator_, 'filename.pkl', compress = 1)
# generator("Matt has", do_sample=True, min_length=50)