import numpy as np
from sklearn.svm import SVC

# 1. Dataset con el nuevo punto [5, 5] etiquetado como Clase 0
X = np.array([
    [2, 2],
    [3, 3],
    [4, 2],
    [6, 6],
    [7, 8],
    [8, 7],
    [5, 5]  # Punto intercalado para forzar la no linealidad
])

Y = np.array([0, 0, 0, 1, 1, 1, 0])

# 2. Modelo con Kernel RBF (Radial Basis Function)
modelo_rbf = SVC(kernel='rbf')
modelo_rbf.fit(X, Y)

# 3. Extraer Vectores de Soporte que sostienen la frontera curva
vectores_soporte = modelo_rbf.support_vectors_

# 4. Predicción del nuevo punto [5, 4]
punto_prueba = np.array([[5, 4]])
prediccion = modelo_rbf.predict(punto_prueba)

print("Vectores de Soporte identificados por RBF:\n", vectores_soporte)
print(f"El punto {punto_prueba[0]} pertenece a la clase: {prediccion[0]}")