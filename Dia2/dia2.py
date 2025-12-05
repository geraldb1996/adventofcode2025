
def identificador_epico_de_ids_invalidos(numero):
    """
    Verifica si un número está formado por una secuencia de dígitos repetida dos veces.
    Ejemplos: 55 (5, 5), 6464 (64, 64), 123123 (123, 123).
    """
    s = str(numero)
    n = len(s)
    
    # Si la longitud es impar, no puede ser una repetición exacta de dos partes iguales
    if n % 2 != 0:
        return False
    
    mitad = n // 2
    parte1 = s[:mitad]
    parte2 = s[mitad:]
    
    return parte1 == parte2

def main():
    try:
        with open('Dia2/dia2_inputExample.txt', 'r') as f:
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
                    
        except ValueError:
            print(f"Error procesando el rango: {rango_str}")
            continue

if __name__ == "__main__":
    main()
