def cal_discount(subtotal, client_type):
    # Descuento según el monto
    if subtotal >= 1000:
        discount = 0.15
    elif subtotal >= 500:
        discount = 0.10
    else:
        discount = 0.0

    # Descuento adicional por tipo de cliente
    if client_type.lower() == "vip":
        discount += 0.10
    elif client_type.lower() == "frecuente":
        discount += 0.05

    return subtotal * discount
