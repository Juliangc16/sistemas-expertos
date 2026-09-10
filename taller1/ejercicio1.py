estado_cliente = {
    "ingresos": 60000,
    "historial": "Excelente",
    "deuda_activa": 12000,
    "tiene_avalista": True
}

def motor_evaluacion_credito(hechos):

    if hechos["deuda_activa"] > 10000 and not hechos["tiene_avalista"]:
        return "RECHAZADO: Alto riesgo por deuda sin aval."
    if hechos["ingresos"] > 50000 and hechos["historial"] == "Excelente":
        return "APROBADO: Cumple criterios hipotecarios."
    return "REVISIÓN MANUAL: No cumple criterios automáticos."
decision = motor_evaluacion_credito(estado_cliente)
print("Veredicto:", decision)