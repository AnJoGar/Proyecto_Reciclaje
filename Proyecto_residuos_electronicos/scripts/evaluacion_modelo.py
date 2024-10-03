from keras.models import load_model
from joblib import load
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error

# Cargar el modelo
modelo_cargado = load_model('modelo_red_neuronal.h5')

# Cargar el scaler
scaler_cargado = load('scaler.joblib')

# Preparar nuevos datos
X_nuevos_datos = pd.DataFrame({
    'AñoProyeccion': [2025, 2026, 2024],
    'Ingresos': [600, 47000, 49000],
   # 'Edad': [25, 30, 35],
    'Ocupacion': [1, 1, 1],
    'AreaResidencia': [2, 1, 1],
    'NivelEducativo':[2, 1, 1],
    'FrecuenciaReciclaje':[1, 1, 1],
    'Televisor_Desechado': [1, 1, 1],
    'Computadora_Desechado': [1, 1, 1],
    'Baterías_Desechado': [1, 1, 1],
    'Teléfono móvil básico_Desechado': [1, 1, 1],
    'Console de videojuegos_Desechado': [1, 1, 1],
    'Tablet_Desechado': [1, 1, 1],
    'Teléfono móvil inteligente_Desechado': [1, 1, 1],
    'Electrodomésticos inteligentes (nevera, lavadora, etc.)_Desechado': [1, 1, 1],
    'Dispositivos de domótica (asistentes de voz, termostatos inteligentes, etc.)_Desechado': [0, 0, 0],
    'Otra_Desechado': [0, 0, 0]
})

# Comprobar nombres de características del scaler
print("Nombres de características usados durante el entrenamiento:")
print(scaler_cargado.feature_names_in_)

# Asegurarse de que los nombres y el orden de las características coincidan
X_nuevos_datos = X_nuevos_datos[scaler_cargado.feature_names_in_]

# Normalizar los nuevos datos
X_nuevos_datos_scaled = scaler_cargado.transform(X_nuevos_datos)

# Realizar predicciones
y_pred_nuevos = modelo_cargado.predict(X_nuevos_datos_scaled)

# Añadir las predicciones al DataFrame original
X_nuevos_datos['Prediccion_Residuos'] = y_pred_nuevos

# Simular los valores reales (estos deben ser reemplazados por tus valores reales para calcular las métricas)
# Aquí simplemente se coloca un ejemplo para fines demostrativos
y_true = [5.905727,73.665573, 76.601913]  # Debes reemplazar estos valores con los reales que tengas

# Calcular R² y MSE
r2 = r2_score(y_true, y_pred_nuevos)
mse = mean_squared_error(y_true, y_pred_nuevos)

# Mostrar las métricas de rendimiento
print(f"R² Score: {r2}")
print(f"Mean Squared Error: {mse}")
# Mostrar todas las predicciones
print("Predicciones:")
print(X_nuevos_datos[['AñoProyeccion', 'Ingresos', 'Prediccion_Residuos']])