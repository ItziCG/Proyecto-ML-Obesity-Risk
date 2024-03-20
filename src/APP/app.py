from flask import Flask
import pickle

model=pickle.load(open('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/model.pkl','rb'))

print(model)

app= Flask(__name__)

@app.route('/',methods=['GET'])
def home():
   return '<h1>PREDICCIÓN DEl NIVEL DE SOBREPESO</h1>'

@app.route('/predict', methods=['POST'])
def predict():

   return model