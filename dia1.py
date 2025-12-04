# Advent of Code 2025 - Día uno
# Vamo a meter las 4000 y la madre de entradas en un TXT y leero con python, que chille

pointer_donde_esta_apuntando_el_coso = 50
contador_de_cuantas_veces_el_pointer_llego_a_0 = 0
contador_de_lineas = 0

# Abrimos el input hijuesumauser
try:
    with open("ejemplo.txt", "r") as f:
        for linea in f:
            contador_de_lineas += 1
            linea = linea.strip() # Eliminamos espacios en blanco y saltos de linea
            if not linea:
                continue

            # Obtenemos la dirección (L o R) y la cantidad de pasos
            direccion = linea[0]
            pasos = int(linea[1:])

            # Simulamos el movimiento paso a paso
            for _ in range(pasos):
                if direccion == "L":
                    # Si baja de 0, va a 99
                    if pointer_donde_esta_apuntando_el_coso < 0:
                        pointer_donde_esta_apuntando_el_coso = 99
                    pointer_donde_esta_apuntando_el_coso -= 1
                elif direccion == "R":
                    # Si sube de 99, va a 0
                    if pointer_donde_esta_apuntando_el_coso > 99:
                        pointer_donde_esta_apuntando_el_coso = 0
                    pointer_donde_esta_apuntando_el_coso += 1
                # Verificamos si el pointer es 0 después del movimiento
                if pointer_donde_esta_apuntando_el_coso == 0:
                    contador_de_cuantas_veces_el_pointer_llego_a_0 += 1

    print(f"Valor final del pointer: {pointer_donde_esta_apuntando_el_coso}")
    print(f"Veces que el pointer llegó a 0: {contador_de_cuantas_veces_el_pointer_llego_a_0}")
    print(f"Total de lineas leidas: {contador_de_lineas}")

except FileNotFoundError:
    print("Error: No se encontró el archivo input.txt")
except ValueError:
    print("Error: Formato de linea inválido en input.txt")
