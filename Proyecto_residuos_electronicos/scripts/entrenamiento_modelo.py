import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from joblib import load, dump
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
from django.conf import settings 
# Cargar las variables
X = load('X_variables.joblib')
y = load('y_variable.joblib')

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Guardar el scaler
dump(scaler, 'scaler.joblib')
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
# Crear el modelo de la red neuronal
modelo_nn = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)  # Capa de salida
])

# Compilar el modelo
modelo_nn.compile(optimizer='adam', loss='mean_squared_error')
# Entrenar el modelo y guardar el historial
historial = modelo_nn.fit(X_train, y_train, epochs=200, batch_size=32, verbose=1)
# Realizar predicciones en el conjunto de prueba
predicciones = modelo_nn.predict(X_test)
# Guardar el historial en un archivo
np.save('historial_entrenamiento.npy', historial.history)

# Calcular métricas de evaluación usando el conjunto de prueba
mse = mean_squared_error(y_test, predicciones)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predicciones)
modelo_nn.summary()
if hasattr(X, 'columns'):
    print("Columnas con las que se entrenó el modelo:", X.columns)
else:
    # Si es una matriz numpy, imprime la forma y las primeras filas para revisar
    print("Forma del conjunto de datos X:", X.shape)
    print("Primeras filas del conjunto de datos X:")
    print(X[:5])
print(f"Error Cuadrático Medio (MSE): {mse:.4f}")
print(f"Raíz del Error Cuadrático Medio (RMSE): {rmse:.4f}")
print(f"Coeficiente de Determinación (R²): {r2:.4f}")
print("Número de características:", scaler.n_features_in_)
print("Nombres de características:", scaler.feature_names_in_)
modelo_nn.save('modelo_residuos_electronicos.h5')
# Guardar el historial en un archivo
np.save('historial_entrenamiento.npy', historial.history)
