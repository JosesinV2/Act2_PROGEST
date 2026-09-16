from calculate_subtotal import calcular_subtotal
from calculate_discount import calcular_descuento
from calculate_shipping import calcular_envio
from validations import pedir_texto, pedir_numero, pedir_entero, pedir_opcion_menu

def main():
    print("=== DATOS DEL CLIENTE ===")
    cliente = pedir_texto("Nombre del cliente: ")
    
    # Menú para Tipo de Cliente
    print("\n--- Tipo de Cliente ---")
    tipos_permitidos = ["Regular", "Frecuente", "VIP"]
    tipo_cliente = pedir_opcion_menu(tipos_permitidos)

    # Menú para Zona de Envío
    print("\n--- Zona de Envío ---")
    zonas_permitidas = ["Local", "Nacional", "Internacional"]
    zona = pedir_opcion_menu(zonas_permitidas)

    print("\n=== DATOS DEL PRODUCTO ===")
    producto = pedir_texto("Nombre del producto: ")
    precio = pedir_numero("Precio unitario: $")
    cantidad = pedir_entero("Cantidad: ")

    # Cálculos
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal, tipo_cliente)
    envio = calcular_envio(zona)
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

if __name__ == "__main__":
    main()