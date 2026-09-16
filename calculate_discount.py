def cal_discount(subtotal, client_type):
    # Descuento según el monto
    if subtotal >= 1000:
        desc = 0.15
    elif subtotal >= 500:
        desc = 0.10
    else:
        desc = 0.0

    # Descuento adicional por tipo de cliente
    if client_type.lower() == "vip":
        desc += 0.10
    elif client_type.lower() == "frecuente":
        desc += 0.05

    return subtotal * desc