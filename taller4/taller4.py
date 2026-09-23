# 1. Grados de membresía simulados tras la Fuzzificación
grados_rh = {
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.5,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.3,
    "antiguedad_larga": 0.6
}

# 2. Evaluación de Reglas con T-Normas (min) y T-Conormas (max)
def motor_inferencia_rh(grados):
    # R1: SI Desempeño es Pobre O Antigüedad es Corta -> Bono Bajo
    bono_bajo = max(grados["desempeno_pobre"], grados["antiguedad_corta"])
    
    # R2: SI Desempeño es Promedio -> Bono Medio
    bono_medio = grados["desempeno_promedio"]
    
    # R3: SI Desempeño es Excelente Y Antigüedad es Larga -> Bono Alto
    bono_alto_r3 = min(grados["desempeno_excelente"], grados["antiguedad_larga"])
    
    # Supongamos una segunda regla R4 que también concluye en Bono Alto con fuerza 0.4
    bono_alto_r4 = 0.4
    
    # Paso de Agregación de Mamdani usando la T-Conorma (OR / max) para Bono Alto
    bono_alto_final = max(bono_alto_r3, bono_alto_r4)
    
    return {
        "Bono Bajo": bono_bajo,
        "Bono Medio": bono_medio,
        "Bono Alto": bono_alto_final
    }

# 3. Ejecución del motor e impresión de fuerzas de activación
resultados = motor_inferencia_rh(grados_rh)
print("Niveles de activación para cada conclusión:")
print(resultados)