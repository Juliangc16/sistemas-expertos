import numpy as np

# 1. Función de activación Escalón
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

# 2. Función del Perceptrón (Forward Pass)
def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    salida = funcion_escalon(Z)
    return salida

# 3. Pesos y Sesgo ajustados para resolver la Compuerta OR
pesos_or = np.array([0.5, 0.5])
sesgo_or = -0.2

# 4. Evaluación de las 4 combinaciones de la tabla de verdad
entradas = [
    np.array([0, 0]),
    np.array([0, 1]),
    np.array([1, 0]),
    np.array([1, 1])
]

print("--- Evaluación de la Compuerta OR ---")
for x in entradas:
    resultado = perceptron(x, pesos_or, sesgo_or)
    print(f"Entrada: {x} -> Salida del Perceptrón: {resultado}")