hechos = {
    "tiene_motor": True,
    "tiene_dos_ruedas": True,
    "es_menor_de_edad": True
}

reglas = [
    {
        "id": "R1",
        "condiciones": ["tiene_motor", "tiene_dos_ruedas"],
        "conclusion": "es_motocicleta"
    },
    {
        "id": "R2",
        "condiciones": ["es_motocicleta"],
        "conclusion": "requiere_casco"
    },
    {
        "id": "R3",
        "condiciones": ["requiere_casco", "es_menor_de_edad"],
        "conclusion": "permiso_denegado"
    }
]

ciclo = 1

while True:
    nuevo_hecho = False

    for regla in reglas:
        if regla["conclusion"] in hechos:
            continue

        if all(hechos.get(condicion, False) for condicion in regla["condiciones"]):
            conclusion = regla["conclusion"]
            hechos[conclusion] = True
            nuevo_hecho = True

            print(f"Ciclo {ciclo} → {regla['id']} → {conclusion}")

    if not nuevo_hecho:
        break

    ciclo += 1

print("\nMemoria final:")
for hecho, valor in hechos.items():
    print(f"{hecho}: {valor}")