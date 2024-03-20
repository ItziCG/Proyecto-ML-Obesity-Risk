from flask import Flask
import pickle
import os

os.chdir(os.path.dirname(__file__))

print(os.getcwd())

model=pickle.load(open('best_model.pkl','rb'))

print(model)

app= Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return '<h1>PREDICCIÓN DEl NIVEL DE SOBREPESO</h1>'

@app.route('/predict', methods=['POST'])
def predict():

    return model