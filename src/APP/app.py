from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo previamente entrenado
col_label=joblib.load('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/col_label.pkl')
col_ohe=joblib.load('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/col_ohe.pkl')
esc_columns= joblib.load('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/esc_columns.pkl')
label_encoder=joblib.load('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/label_encoder.pkl')
minmax_scaler=joblib.load('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/minmax_scaler.pkl')
onehot_encoder=joblib.load('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/onehot_encoder.pkl')
modelo = joblib.load('/Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/model/best_model.pkl')

# Definir el mapeo para traducir las respuestas del usuario
traducciones = {
    'genero': {'masculino': 'Male', 'femenino': 'Female'},
    'antecedentes_obesidad': {'si': 'yes', 'no': 'no'},
    'consumo_calorias': {'si': 'yes', 'no': 'no'},
    'consumo_entre_comidas': {'Mo': 'Sometimes', 'A veces': 'Sometimes', 'Frecuentemente': 'Frequently', 'Siempre': 'Always'},
    'fumador': {'si': 'yes', 'no': 'no'},
    'monitoreo_calorias': {'si': 'yes', 'no': 'no'},
    'consumo_alcohol': {'No': 'no', 'A veces': 'Sometimes', 'Frecuentemente': 'Frequently'},
    'consumo_entre_comidas': {'Nunca':'no', 'A veces':'Sometimes', 'Frecuentemente':'Frequently', 'Siempre':'Always'},
    'medio_transporte':{'Caminar':'Walking', 'Bicileta':'Bike', 'Moto':'Motorbike', 'Coche':'Automobile', 'Transporte Público':'Public_Transportation'}
}

# Definir las columnas del DataFrame
columnas = ['gender', 'age', 'height', 'weight',
            'family', 'favc', 'fcvc', 'ncp', 'caec',
            'smoke', 'ch2o', 'scc', 'faf', 'tue', 'calc', 'mtrans']

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/prediccion', methods=['POST'])
def predecir_obesidad():
    if request.method == 'POST':
        # Obtener una respuesta del usuario
        datos = {
            'gender': traducciones['genero'][request.form['genero']],
            'age': int(request.form['edad']),
            'height': float(request.form['altura']),
            'weight': float(request.form['peso']),
            'family': traducciones['antecedentes_obesidad'][request.form['antecedentes_obesidad']],
            'favc': traducciones['consumo_calorias'][request.form['consumo_calorias']],
            'fcvc': int(request.form['ingesta_vegetales']),
            'ncp': int(request.form['num_comidas_principales']),
            'caec': traducciones['consumo_entre_comidas'][request.form['consumo_entre_comidas']],
            'smoke': traducciones['fumador'][request.form['fumador']],
            'ch2o': int(request.form['consumo_agua_diario']),
            'scc': traducciones['monitoreo_calorias'][request.form['monitoreo_calorias']],
            'faf': int(request.form['frecuencia_actividad_fisica']),
            'tue': int(request.form['tiempo_uso_tecnologico']),
            'calc': traducciones['consumo_alcohol'][request.form['consumo_alcohol']],
            'mtrans': request.form['medio_transporte']
        }

        # Crear un DataFrame con la respuesta del usuario
        df_usuario = pd.DataFrame([datos], columns=columnas)

        #Transformaciones
        df_transformado = df_usuario.copy()
        df_transformado[esc_columns] = minmax_scaler.transform(df_transformado[esc_columns])
        transformed_df= onehot_encoder.transform(df_transformado[col_ohe])
        transformed_df_ohe = pd.DataFrame(transformed_df, columns=onehot_encoder.get_feature_names_out(col_ohe), index=df_transformado.index)
        df_trans= pd.concat([df_transformado, transformed_df_ohe], axis=1).drop(columns=col_ohe)
        
        for column in col_label:
            df_trans[column] = label_encoder.transform(df_trans[column])
          

        # Realizar la predicción utilizando el modelo y el DataFrame del usuario
        resultado = modelo.predict(df_trans)

        # Convertir el resultado a una etiqueta legible
        mapeo_resultados = {0: 'Peso bajo', 1: 'Peso ideal', 2: 'Obesidad tipo I', 3:'Obesidad tipo II', 4:'Obesidad tipo III', 5:'Sobrepeso nivel I', 6:'Sobrepeso nivel II'}

        # Convertir el resultado a una etiqueta legible
        nivel_obesidad = mapeo_resultados.get(resultado, 'Desconocido')

        # Renderizar la plantilla de resultado y pasar el nivel de obesidad
        return render_template('result.html', nivel_obesidad=nivel_obesidad)

if __name__ == '__main__':
    app.run(debug=True)
