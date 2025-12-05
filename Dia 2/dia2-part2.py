def identificador_epico_de_ids_invalidos(numero):
    """
    Verifica si un número está formado por una secuencia de dígitos repetida al menos dos veces.
    Ejemplos: 12341234 (2 veces), 123123123 (3 veces), 1111111 (7 veces).
    """
    s = str(numero)
    n = len(s)
    
    # Probar longitudes de subcadena desde 1 hasta n/2
    for length in range(1, n // 2 + 1):
        # Si la longitud total no es divisible por la longitud de la subcadena, no puede ser una repetición exacta
        if n % length == 0:
            subcadena = s[:length]
            repeticiones = n // length
            if subcadena * repeticiones == s:
                return True
                
    return False

def main():
    suma_total_para_resolver_el_asertijo = 0
    numeros_concatenados = ""
    try:
        with open('Dia2/input_dia2.txt', 'r') as f:
            contenido = f.read().strip()
    except FileNotFoundError:
        print("Error: No se encontró el archivo input_dia2.txt")
        return

    # El formato es "id1-id2,id3-id4,..."
    if not contenido:
        return

    rangos_str = contenido.split(',')
    
    for rango_str in rangos_str:
        try:
            inicio_str, fin_str = rango_str.split('-')
            inicio = int(inicio_str)
            fin = int(fin_str)
            
            # Iterar sobre el rango (asumiendo inclusivo según la descripción típica de rangos)
            # "da un rango empezando en id1 y termina en id2" -> usualmente inclusivo
            for num in range(inicio, fin + 1):
                if identificador_epico_de_ids_invalidos(num):
                    print(num)
                    suma_total_para_resolver_el_asertijo += num
                    print(f"keloke, la respuesta es: {suma_total_para_resolver_el_asertijo}")
                    #numeros_concatenados += str(num)
                    
        except ValueError:
            print(f"Error procesando el rango: {rango_str}")
            continue

    print(f"Números concatenados: {numeros_concatenados}")

if __name__ == "__main__":
    main()
