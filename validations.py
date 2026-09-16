def get_text(message):
    """Pide un texto y valida que solo contenga letras y espacios."""
    while True:
        texto = input(message).strip()
        if texto and texto.replace(" ", "").isalpha():
            return texto
        print("Error: Ingrese un nombre válido (solo letras).")

def get_number(message):
    """Pide un número flotante y asegura que sea positivo."""
    while True:
        try:
            val = float(input(message))
            if val > 0:
                return val
            print("Debe ser mayor a 0.")
        except ValueError:
            print("Ingrese un número válido.")

def pedir_entero(mensaje):
    """Pide un número entero positivo para las cantidades."""
    return int(pedir_numero(mensaje))

def pedir_opcion_menu(opciones):
    """Muestra un menú numerado y valida que el usuario elija una opción válida."""
    print("Seleccione una opción:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"  {i}. {opcion}")
    
    while True:
        try:
            seleccion = int(input("Opción: "))
            if 1 <= seleccion <= len(opciones):
                return opciones[seleccion - 1]  # Devuelve el texto de la opción elegida
            print(f"Por favor, elija un número entre 1 y {len(opciones)}.")
        except ValueError:
            print("Entrada inválida. Ingrese solo el número de la opción.")
