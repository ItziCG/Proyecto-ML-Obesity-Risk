Proyecto_ML_Obesity_Risk
==============================

Proyecto de machine learning sobre el nivel de obesidad.

Este análisis se centra en el estudio de los registros de individuos aleatorios, a partir de características fisiológicas y hábitos de los mismos.

Como principal objetivo se desea predecir el riesgo de obesidad en el que se encuentran los individuos, para así poder evitar complicaciones de salud a futuro.Para ello emplearemos técnicas de Machine Learning.

<p align="center">
  <img src="https://www-rockandpop-cl.cdn.ampproject.org/i/s/www.rockandpop.cl/wp-content/uploads/2019/10/obesidad-y-sobrepeso-como-prevenir.jpg" alt="Texto alternativo" width="600" height="300">
</p>


Organización de las carpetas
------------

    ├── LICENSE
    ├── README.md          <- presentación y estructura del proyecto para los usuarios.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src               
    │   │
    │   ├── data           
    │   │   ├── processed        <- dataset limpio preparado para modelar
            └── raw              <- dataset en crudo

    │   ├── model  
    │   │   ├── best_model.pkl   <-mejor modelo entrenado listo para poner en producción

    │   ├── models 
            ├── train.py         <- entrenamiento del mejor modelo      

    │   ├── utils                <- módulos y funciones auxiliares     
    │   │
    │   │
    │   ├── notebooks        
    │       └── proyect_resume.ipynb (Memoria del proyecto, incluye EDA, pasos explicados, búsqueda del mejor modelo)

--------
