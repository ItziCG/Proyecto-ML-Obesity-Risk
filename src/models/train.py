# Tratamiento de datos
import pandas as pd

# Modelos
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler
from xgboost import XGBClassifier
import joblib

#Carga de datos
df=pd.read_csv('src/data/raw/train.csv')


#Pasamos los nombres de las columnas a minúscula
df.columns = df.columns.str.lower()

#Renombramos 'family_history_with_overweight'
df = df.rename(columns={'family_history_with_overweight': 'family'})

# Separar características y etiquetas para conjunto de entrenamiento
X_train = df.drop(['nobeyesdad','id'], axis=1)
y_train = df['nobeyesdad']


#Columnas a procesar
col_label = ['caec', 'calc','mtrans']
col_ohe = ['gender', 'family', 'favc','smoke','scc']
esc_columns= ['age', 'weight','height','fcvc','ncp','ch2o','faf','tue']

joblib.dump(col_label, 'src/model/col_label.pkl')
joblib.dump(col_ohe, 'src/model/col_ohe.pkl')
joblib.dump(esc_columns, 'src/model/esc_columns.pkl')

#Aplicamos MinMaxScaler
esc = MinMaxScaler()
X_train[esc_columns] = esc.fit_transform(X_train[esc_columns])

joblib.dump(esc, 'src/model/minmax_scaler.pkl')

#Aplicamos OneHot
ohe = OneHotEncoder(drop='first',sparse_output=False, handle_unknown='ignore')

ohe.fit(X_train[col_ohe])

transformed_X_train = ohe.transform(X_train[col_ohe])
transformed_df = pd.DataFrame(transformed_X_train, columns=ohe.get_feature_names_out(col_ohe), index=X_train.index)
X_train_trans= pd.concat([X_train, transformed_df], axis=1).drop(columns=col_ohe)

joblib.dump(ohe, 'src/model/onehot_encoder.pkl')


label_encoder = LabelEncoder()
label_encoders = {}
for column in col_label:
    X_train_trans[column] = label_encoder.fit_transform(X_train_trans[column])
    label_encoders[column] = label_encoder

joblib.dump(label_encoders, 'src/model/label_encoders.pkl')


#Aplicamos labelEncoder a la target
y_train_trans = label_encoder.fit_transform(y_train)

#Entrenamos el modelo con los mejores hiperparámetros escogidos

XGB_model = XGBClassifier(learning_rate= 0.1, max_depth= 4, n_estimators= 200, alpha=0.1, reg_lambda=0.5)
XGB_model.fit(X_train_trans, y_train_trans)


# Guardar el modelo
joblib.dump(XGB_model, 'src/model/best_model.pkl')
