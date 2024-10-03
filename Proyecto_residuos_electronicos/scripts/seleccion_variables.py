import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import dump

# Cargar el archivo CSV
url = '../data/dataframe_limpio copy.csv'

# Leer el archivo CSV con las configuraciones correctas
df = pd.read_csv(url)

# Configurar pandas para mostrar todas las filas y columnas (opcional)
pd.set_option('display.max_rows', None)  # Mostrar todas las filas
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas

# Verificar columnas y valores nulos
valores_nulos = df.isnull().sum()
print("Valores nulos por columna:")
print(valores_nulos[valores_nulos > 0])

# Imprimir el dataframe completo (opcional, para verificar los datos)
##print(df)
# Agregar una nueva columna para el crecimiento proyectado de productos desechados
# Suponiendo que ya has definido Tasa_Crecimiento
Tasa_Crecimiento = 0.33  # Ejemplo de tasa de crecimiento

# Crear una nueva columna en df antes de definir X y y
df['Tasa_Crecimiento'] = Tasa_Crecimiento

# Variables predictoras (entrantes)
X = df[[  'AñoProyeccion'
          ,'Ingresos','NivelEducativo','Ocupacion','AreaResidencia','FrecuenciaReciclaje','Televisor_Desechado','Computadora_Desechado',
                      'Baterías_Desechado','Teléfono móvil básico_Desechado','Console de videojuegos_Desechado',
                      'Tablet_Desechado','Teléfono móvil inteligente_Desechado',
                       'Electrodomésticos inteligentes (nevera, lavadora, etc.)_Desechado',
                      'Dispositivos de domótica (asistentes de voz, termostatos inteligentes, etc.)_Desechado',
                        'Otra_Desechado'

  ]]

# Variable de salida (cantidad de residuos electrónicos desechados)
#y = df['TotalProductosDesechados']  # Asegúrate de que esta columna exista
y = df['TotalProductosDesechados'] * (1 + Tasa_Crecimiento) 
# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Imprimir las dimensiones de los conjuntos de entrenamiento y prueba (opcional)
print("Tamaño del conjunto de entrenamiento:", X_train.shape)
print("Tamaño del conjunto de prueba:", X_test.shape)
# Guardar las variables
dump(X, 'X_variables.joblib')
dump(y, 'y_variable.joblib')