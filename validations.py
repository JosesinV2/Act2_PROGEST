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

def askfor_int(mesaje):
    """Pide un número entero positivo para las cantidades."""
    return int(pedir_numero(mesaje))

def askfor_option_onmenu(opciones):
    """Muestra un menú numerado y valida que el usuario elija una opción válida."""
    print("Seleccione una opción:")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")
    
    while True:
        try:
            selection = int(input("Option: "))
            if 1 <= selection <= len(options):
                return options[selection - 1]  # Devuelve el texto de la opción elegida
            print(f"Por favor, elija un número entre 1 y {len(options)}.")
        except ValueError:
            print("Entrada inválida. Ingrese solo el número de la opción.")
