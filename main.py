import calculate_subtotal
import calculate_discount
import calculate_shipping
import validations

def main():
    print("=== DATOS DEL CLIENTE ===")
    cliente = validations.get_text("Nombre del cliente: ")

    # Menú para Tipo de Cliente
    print("\n--- Tipo de Cliente ---")
    tipos_permitidos = ["Regular", "Frecuente", "VIP"]
    tipo_cliente = validations.askfor_option_onmenu(tipos_permitidos)

    # Menú para Zona de Envío
    print("\n--- Zona de Envío ---")
    zonas_permitidas = ["Local", "Nacional", "Internacional"]
    zona = validations.askfor_option_onmenu(zonas_permitidas)

    print("\n=== DATOS DEL PRODUCTO ===")
    producto = validations.get_text("Nombre del producto: ")
    precio = validations.get_number("Precio unitario: $")
    cantidad = validations.askfor_int("Cantidad: ")

    # Cálculos
    subtotal = calculate_subtotal.cal_subtotal(precio, cantidad)
    descuento = calculate_discount.cal_discount(subtotal, tipo_cliente)
    envio = calculate_shipping.shipping_fee(zona)
    total = subtotal - descuento + envio

    # Resumen
    print("\n" + "=" * 30)
    print("   RESUMEN DE COTIZACIÓN   ")
    print("=" * 30)
    print(f"Cliente:   {cliente}")
    print(f"Tipo:      {tipo_cliente}")
    print(f"Zona:      {zona}")
    print(f"Producto:  {producto} (x{cantidad})")
    print("-" * 30)
    print(f"Subtotal:  C${subtotal:.2f}")
    print(f"Descuento: -C${descuento:.2f}")
    print(f"Envío:     +C${envio:.2f}")
    print("-" * 30)
    print(f"TOTAL:     C${total:.2f}")
    print("=" * 30)


main()