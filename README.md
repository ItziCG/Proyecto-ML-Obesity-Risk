Proyecto ML Obesity Risk
==============================

Proyecto de machine learning sobre el nivel de obesidad.

Este análisis se centra en el estudio de los registros de individuos aleatorios, a partir de características fisiológicas y hábitos de los mismos.

Como principal objetivo se desea predecir el riesgo de obesidad en el que se encuentran los individuos, para así poder evitar complicaciones de salud a futuro.Para ello emplearemos técnicas de Machine Learning.

<p align="center">
  <img src="https://www-rockandpop-cl.cdn.ampproject.org/i/s/www.rockandpop.cl/wp-content/uploads/2019/10/obesidad-y-sobrepeso-como-prevenir.jpg" alt="Texto alternativo" width="600" height="300">
</p>


Organización de las carpetas
------------

    ├── src               
    │   │
    │   ├── App              <- Carpeta para la creacción de app con Flask          
    │   │   ├── templates
    │   │   │     ├── formulario.html
    │   │   │     ├── index.html
    │   │   │     └── result.html
    │   │   │
    │   │   ├── app.py         <- código de aplicación con Flask
    │   │   │
    │   │   │
    │   │   └── Dockerfile     <- instrucciones para construir imagen Docker
    │   │   
    │   │   
    │   ├── data           
    │   │   ├── processed        <- dataset limpio preparado para modelar
    │   │   └── raw              <- dataset en crudo
    │   │
    │   │
    │   ├── model  
    │   │   ├── best_model.pkl      <- mejor modelo entrenado listo para poner en producción
    │   │   ├── col_label.pkl       <- columnas label Encoder
    │   │   ├── col_ohe.pkl         <- columnas one hot Encoder
    │   │   ├── esc_columns.pkl     <- columnas a escalar
    │   │   ├── label_encoder.pkl   <- label Encoder entrenado
    │   │   ├── minmax_scaler.pkl   <- MinMax Escaler entrenado
    │   │   └── onehot_encoder.pkl  <- one hot Encoder entrenado
    │   │   
    │   │
    │   │
    │   ├── models 
    │   │   ├── train.py            <- entrenamiento del mejor modelo      
    │   │  
    │   │
    │   ├── notebooks        
    │   │   └── proyect_resume.ipynb  <- (Memoría del proyecto-> EDA, pasos explicados, búsqueda del mejor modelo)
    │   │
    │   │
    │   ├── utils                    <- módulos y funciones auxiliares
    │   │ 
    │   │
    │   │ 
    │   └── presentación
    │       ├── images              <- imágenes del notebook de los gráficos guardadas
    │       └── obesity_ml.pptx     <- Power point exposición proyecto
    │      
    │
    │  
    ├── LICENSE
    │   
    │   
    ├── README.md          <- presentación y estructura del proyecto y sus carpetas para los usuarios.
    │
    │   
    ├── requirements.txt   <- The requirements file (librerías y paquetes utilizados en el proyecto)
    │     
    │

--------
