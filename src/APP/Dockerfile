FROM python:3.12

# Establece el directorio de trabajo en /Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/App
WORKDIR /Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/App

# Copia el archivo de requisitos de la aplicación al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el contenido actual del directorio al contenedor
COPY . .

# Expone el puerto 5000 en el contenedor
EXPOSE 5000

# Ejecuta la aplicación Flask cuando se inicie el contenedor
CMD ["python3", "app.py"]

