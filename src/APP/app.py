from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo previamente entrenado
modelo = joblib.load('modelo_obesidad.joblib')

# Definir las columnas del DataFrame
columnas = ['Genero', 'Edad', 'Altura', 'Peso', 'Antecedentes_obesidad', 'Consumo_calorias',
            'Ingesta_vegetales', 'Num_comidas_principales', 'Consumo_entre_comidas', 'Fumador',
            'Consumo_agua_diario', 'Monitoreo_calorias', 'Frecuencia_actividad_fisica',
            'Tiempo_uso_tecnologico', 'Consumo_alcohol', 'Medio_transporte']

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/prediccion', methods=['POST'])
def predecir_obesidad():
    if request.method == 'POST':
        # Obtener una respuesta del usuario
        datos = {
            'gender': request.form['genero'],
            'age': int(request.form['edad']),
            'height': float(request.form['altura']),
            'weight': float(request.form['peso']),
            'family': request.form['antecedentes_obesidad'],
            'favc': request.form['consumo_calorias'],
            'fcvc': int(request.form['ingesta_vegetales']),
            'ncp': int(request.form['num_comidas_principales']),
            'caec': request.form['consumo_entre_comidas'],
            'smoke': request.form['fumador'],
            'ch2o': int(request.form['consumo_agua_diario']),
            'scc': request.form['monitoreo_calorias'],
            'faf': int(request.form['frecuencia_actividad_fisica']),
            'tue': int(request.form['tiempo_uso_tecnologico']),
            'calc': request.form['consumo_alcohol'],
            'mtrans': request.form['medio_transporte']
        }

        # Crear un DataFrame con la respuesta del usuario
        df_usuario = pd.DataFrame([datos], columns=columnas)

        # Realizar la predicción utilizando el modelo y el DataFrame del usuario
        resultado = modelo.predict(df_usuario)

        # Convertir el resultado a una etiqueta legible
        if resultado == 0:
            nivel_obesidad = 'Bajo'
        elif resultado == 1:
            nivel_obesidad = 'Medio'
        else:
            nivel_obesidad = 'Alto'

        # Renderizar la plantilla de resultado y pasar el nivel de obesidad
        return render_template('resultado.html', nivel_obesidad=nivel_obesidad)

if __name__ == '__main__':
    app.run(debug=True)

