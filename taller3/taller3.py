# 1. Definición de la función de membresía triangular
def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    elif x == b:
        return 1.0

# 2. Arreglo de conductores con sus años de experiencia a evaluar
conductores_experiencia = [3, 6, 12]

# 3. Evaluación de cada conductor mediante un ciclo for
for anos in conductores_experiencia:
    # Definición de los conjuntos difusos para Novato (0,0,5), Intermedio (2,5,8) y Experto (5,10,20)
    novato = membresia_triangular(anos, 0, 0, 5)
    intermedio = membresia_triangular(anos, 2, 5, 8)
    experto = membresia_triangular(anos, 5, 10, 20)
    
    # Determinación de la categoría dominante usando la función max()
    grados = {'Novato': novato, 'Intermedio': intermedio, 'Experto': experto}
    categoria_dominante = max(grados, key=grados.get)
    
    # Impresión de resultados
    print(f"Conductor con {anos} años de experiencia:")
    print(f"  - Novato: {novato:.2f}, Intermedio: {intermedio:.2f}, Experto: {experto:.2f}")
    print(f"  -> Categoría asignada: {categoria_dominante}\n")