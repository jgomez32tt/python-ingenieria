
# Mi primer programa en Python
# Calculadora de consumo de combustible

def calcular_consumo(galones, horas):
    return galones / horas


if __name__ == "__main__":
    print("=== CALCULADORA DE COMBUSTIBLE ===")

    try:
        # Datos del equipo
        galones = float(input("Ingrese los galones de combustible: "))
        horas = float(input("Ingrese las horas de operación: "))

        if galones >= 0 and horas > 0:
            # Calculo del consumo promedio
            consumo = calcular_consumo(galones, horas)

            # Mostrar resultados
            print("Galones suministrados:", galones)
            print("Horas de operacion:", horas)
            print("Consumo promedio:", consumo, "gal/h")
        else:
            print("Los galones deben ser mayores o iguales a cero y las horas mayores que cero.")

    except ValueError:
        print("Entrada inválida. Ingrese números y use punto para los decimales.")
  
