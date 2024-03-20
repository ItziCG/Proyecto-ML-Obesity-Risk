from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Cargar el modelo
model = pickle.load(open('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener los valores ingresados por el usuario desde el formulario
        age = float(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        fcvc = float(request.form['fcvc'])
        ncp = float(request.form['ncp'])
        caec = request.form['caec']
        ch2o = float(request.form['ch2o'])
        faf = float(request.form['faf'])
        tue = float(request.form['tue'])
        calc = request.form['calc']
        mtrans = request.form['mtrans']
        gender_male = 1 if request.form['gender'] == 'Male' else 0
        family_yes = 1 if request.form['family'] == 'Yes' else 0
        favc_yes = 1 if request.form['favc'] == 'Yes' else 0
        smoke_yes = 1 if request.form['smoke'] == 'Yes' else 0
        scc_yes = 1 if request.form['scc'] == 'Yes' else 0
        
        
        # Realizar la predicción con el modelo
        prediction = model.predict([[age, height, weight, fcvc, ncp, caec, ch2o, faf, tue, calc, mtrans, gender_male, family_yes, favc_yes, smoke_yes, scc_yes]])[0]
        
        # Devolver la predicción como respuesta
        return render_template('result.html', prediction=prediction)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
