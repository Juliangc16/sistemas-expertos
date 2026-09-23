import numpy as np

# 1. Función personalizada para calcular el Centroide (Centro de Gravedad - COG)
def calcular_centroide(x, mu):
    numerador = np.sum(x * mu)
    denominador = np.sum(mu)
    if denominador == 0:
        return 0.0
    return numerador / denominador

# 2. Validación con el Taller Analítico (Descuento comercial)
x_analitico = np.array([10, 20, 30, 40])
mu_analitico = np.array([0.2, 0.8, 0.8, 0.0])
descuento_crisp = calcular_centroide(x_analitico, mu_analitico)
print(f"Descuento exacto (Crisp) calculado: {descuento_crisp:.2f}%")

# 3. Escenario: Sistema de frenado automático de un automóvil
x_fuerza = np.linspace(0, 100, 100) # Dominio de 0 a 100 Newtons
# Curva campana de Gauss centrada en 70 Newtons
curva_gauss = np.exp(-0.5 * ((x_fuerza - 70) / 10)**2)

# 4. Defuzzificación de la fuerza de frenado
fuerza_frenado_crisp = calcular_centroide(x_fuerza, curva_gauss)
print(f"Fuerza de frenado exacta a aplicar: {fuerza_frenado_crisp:.2f} Newtons")