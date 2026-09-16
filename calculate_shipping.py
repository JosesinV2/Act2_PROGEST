def shipping_fee(zone):
    zone = zone.lower()
    if zone == "local":
        return 5.0
    elif zone == "nacional":
        return 15.0
    elif zone    == "internacional":
        return 40.0
    return 10.0  # Zona por defecto