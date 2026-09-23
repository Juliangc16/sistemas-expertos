import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 1. Dataset ampliado con 10 clientes y 3 características: [Edad, Salario_Miles, Num_Hijos]
X_entrenamiento = np.array([
    [20, 30, 0],
    [40, 50, 2],
    [35, 45, 1],
    [22, 25, 0],
    [48, 80, 3],
    [52, 90, 2],
    [25, 35, 1],
    [30, 40, 0],
    [45, 60, 2],
    [19, 20, 0]
])

# Etiquetas: 0 = NO COMPRA, 1 = COMPRA
Y_entrenamiento = np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 0])

# 2. Experimentación con K = 1
modelo_knn_1 = KNeighborsClassifier(n_neighbors=1)
modelo_knn_1.fit(X_entrenamiento, Y_entrenamiento)

# 3. Experimentación con K = 5
modelo_knn_5 = KNeighborsClassifier(n_neighbors=5)
modelo_knn_5.fit(X_entrenamiento, Y_entrenamiento)

# 4. Predicción de un cliente nuevo
cliente_nuevo = np.array([[32, 42, 1]])
pred_k1 = modelo_knn_1.predict(cliente_nuevo)
pred_k5 = modelo_knn_5.predict(cliente_nuevo)

print(f"Predicción para el cliente {cliente_nuevo[0]} con K=1: {pred_k1[0]}")
print(f"Predicción para el cliente {cliente_nuevo[0]} con K=5: {pred_k5[0]}")