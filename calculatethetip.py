def calcular_propina(total_factura):
    propina_18 = total_factura * 0.18
    propina_20 = total_factura * 0.20
    propina_25 = total_factura * 0.25

    return propina_18, propina_20, propina_25

def main():
    total_factura = float(input("¿Cuál es el total de la factura de hoy, por favor?: $"))

    propina_18, propina_20, propina_25 = calcular_propina(total_factura)

    print(f"\nPropina del 18% es: ${propina_18:.2f}, lo que hace un total de: ${total_factura + propina_18:.2f}")
    print(f"Propina del 20% es: ${propina_20:.2f}, lo que hace un total de: ${total_factura + propina_20:.2f}")
    print(f"Propina del 25% es: ${propina_25:.2f}, lo que hace un total de: ${total_factura + propina_25:.2f}")

    personas = int(input("\n¿Cuántas personas están involucradas?: "))
    tipo_division = input("¿Deseas dividir la propina y el costo total de manera equitativa o desigual? (equitativa/desigual): ").lower()

    if tipo_division == 'equitativa':  # División equitativa
        propina_por_persona = total_factura / personas
        total_por_persona = (total_factura + propina_18) / personas
        print(f"\nCada persona debería pagar ${propina_por_persona:.2f} como propina y ${total_por_persona:.2f} en total.")
    elif tipo_division == 'desigual':  # División desigual
        porcentaje = float(input("Por favor, ingresa el porcentaje que pagará una persona (sin el signo de porcentaje): "))
        porcentaje /= 100
        total_factura_1 = total_factura * porcentaje
        total_factura_2 = total_factura - total_factura_1
        propina_18_1 = propina_18 * porcentaje
        propina_18_2 = propina_18 - propina_18_1
        print(f"\nLa primera persona debe pagar ${total_factura_1 + propina_18_1:.2f} en total, incluyendo ${propina_18_1:.2f} de propina.")
        print(f"La segunda persona debe pagar ${total_factura_2 + propina_18_2:.2f} en total, incluyendo ${propina_18_2:.2f} de propina.")
    else:
        print("Opción no válida. Por favor, selecciona 'equitativa' para dividir equitativamente o 'desigual' para dividir desigualmente.")

if __name__ == "__main__":
    main()
