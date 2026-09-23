import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Dataset simulado para Marketing: [Edad, Horas_Online, Compras_Previas]
X = np.array([
    [18, 5, 0],
    [45, 1, 3],
    [22, 6, 1],
    [50, 2, 5],
    [19, 8, 0],
    [35, 1, 2],
    [28, 4, 2],
    [60, 1, 0],
    [25, 7, 3],
    [40, 3, 4]
])

# Etiquetas (Y): [1: Hizo clic, 0: Ignoró el anuncio]
Y = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1, 1])

# 2. Inicialización y entrenamiento del Árbol de Decisión
arbol_marketing = DecisionTreeClassifier(max_depth=3)
arbol_marketing.fit(X, Y)

# 3. Extracción e impresión de las reglas lógicas (SI... ENTONCES)
nombres_caracteristicas = ["Edad", "Horas_Online", "Compras_Previas"]
reglas_extraidas = export_text(arbol_marketing, feature_names=nombres_caracteristicas)

print("Base de Reglas generada automáticamente para el Sistema Experto:\n")
print(reglas_extraidas)