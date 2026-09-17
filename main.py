import calculate_subtotal
import calculate_discount
import calculate_shipping
import validations

def main():
    print("=== DATOS DEL CLIENTE ===")
    client = validations.get_text("Nombre del cliente: ")

    # Menú para Tipo de Cliente
    print("\n--- Tipo de Cliente ---")
    allowed_types = ["Regular", "Frecuente", "VIP"]
    client_type = validations.askfor_option_onmenu(allowed_types)

    # Menú para Zona de Envío
    print("\n--- Zona de Envío ---")
    allowed_zones = ["Local", "Nacional", "Internacional"]
    zone = validations.askfor_option_onmenu(allowed_zones)

    print("\n=== DATOS DEL PRODUCTO ===")
    product = validations.get_text("Nombre del producto: ")
    price = validations.get_number("Precio unitario: $")
    amount = validations.askfor_int("Cantidad: ")

    # Cálculos
    subtotal = calculate_subtotal.cal_subtotal(price, amount)
    discount = calculate_discount.cal_discount(subtotal, client_type)
    fee = calculate_shipping.shipping_fee(zone)
    total = subtotal - discount + fee

    # Resumen
    print("\n" + "=" * 30)
    print("   RESUMEN DE COTIZACIÓN   ")
    print("=" * 30)
    print(f"Cliente:   {client}")
    print(f"Tipo:      {client_type}")
    print(f"Zona:      {zone}")
    print(f"Producto:  {product} (x{amount})")
    print("-" * 30)
    print(f"Subtotal:  C${subtotal:.2f}")
    print(f"Descuento: -C${discount:.2f}")
    print(f"Envío:     +C${fee:.2f}")
    print("-" * 30)
    print(f"TOTAL:     C${total:.2f}")
    print("=" * 30)


main()
