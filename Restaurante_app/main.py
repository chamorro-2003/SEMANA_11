from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

## Funciones de interfaz de usuario

def mostrar_menu() -> None:
    print("\n" + "=" * 45)
    print("      SISTEMA DE GESTIÓN DE RESTAURANTE      ")
    print("=" * 45)
    print("1. Registrar Producto")
    print("2. Listar Productos")
    print("3. Registrar Usuario")
    print("4. Listar Usuarios")
    print("5. Realizar Venta")
    print("6. Consultar Ventas por Usuario")
    print("7. Salir")
    print("=" * 45)

### Función principal
def main() -> None:
    servicio_archivo = ArchivoServicio()
    restaurante = Restaurante()

    # Cargar datos existentes desde archivos JSON
    prods = servicio_archivo.cargar_productos()
    usrs = servicio_archivo.cargar_usuarios()
    vts = servicio_archivo.cargar_ventas()
    restaurante.establecer_datos(prods, usrs, vts)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            try:
                p_id = int(input("ID único del producto: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                categoria = input("Categoría: ")
                stock = int(input("Stock inicial: "))

                prod = Producto(p_id, nombre, precio, categoria, stock)
                if restaurante.registrar_producto(prod):
                    servicio_archivo.guardar_productos(restaurante.obtener_productos())
                    print("¡Producto registrado y guardado!")
            except ValueError as e:
                print(f"¡Error de entrada: {e}!")

        elif opcion == "2":
            print("\n--- PRODUCTOS ---")
            lista = restaurante.obtener_productos()
            if not lista:
                print("No hay productos.")
            for p in lista:
                print(p)

        elif opcion == "3":
            try:
                u_id = input("ID/Cédula del Usuario: ")
                nombre = input("Nombre completo: ")
                rol = input("Rol (Ej: Cliente/Admin): ")
                usr = Usuario(u_id, nombre, rol if rol else "Cliente")
                if restaurante.registrar_usuario(usr):
                    servicio_archivo.guardar_usuarios(restaurante.obtener_usuarios())
                    print("¡Usuario registrado y guardado!")
            except ValueError as e:
                print(f"¡Error: {e}!")

        elif opcion == "4":
            print("\n--- USUARIOS ---")
            lista = restaurante.obtener_usuarios()
            if not lista:
                print("No hay usuarios.")
            for u in lista:
                print(u)

        elif opcion == "5":
            try:
                u_id = input("ID/Cédula del Usuario comprador: ")
                p_id = int(input("ID del Producto a comprar: "))
                cant = int(input("Cantidad: "))

                if restaurante.vender_producto(u_id, p_id, cant):
                    # Actualiza tanto ventas.json como el nuevo stock en productos.json
                    servicio_archivo.guardar_productos(restaurante.obtener_productos())
                    servicio_archivo.guardar_ventas(restaurante.obtener_ventas())
            except ValueError as e:
                print(f"¡Error de entrada: {e}!")

        elif opcion == "6":
            u_id = input("Ingrese la identificación del Usuario: ")
            ventas = restaurante.consultar_ventas_usuario(u_id)
            print(f"\n--- VENTAS REGISTRADAS PARA EL USUARIO: {u_id} ---")
            if not ventas:
                print("No se encontraron ventas para este usuario.")
            for v in ventas:
                p = restaurante.buscar_producto(v.producto_id)
                nombre_p = p.nombre if p else "Producto Desconocido"
                print(f"{v} | Producto: {nombre_p}")

        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("¡Error! Opción inválida")


if __name__ == "__main__":
    main()
