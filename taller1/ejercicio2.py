hechos = {
    "ingresos": 60000,
    "historial": "Excelente",
    "deuda_activa": 12000,
    "tiene_avalista": True
}

def evaluar_cliente(hechos):
    if hechos["deuda_activa"]>10000 and not hechos ["tiene_avalista"]:
        return "RECHAZADO"
    if hechos["ingresos"]>50000 and hechos["historial"] == "Excelente":
        return "APROVADO"
    return "REVISION MANUAL"

resultado = evaluar_cliente(hechos)
print ("Resultado:", resultado)