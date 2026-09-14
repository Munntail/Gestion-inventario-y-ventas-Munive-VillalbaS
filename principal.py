import menu
import inventario

archivo_inventario = "inventario.txt"
archivo_ventas = "ventas.txt"

productos = inventario.cargar_datos(archivo_inventario)

while True:
    menu.mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        inventario.alta_producto(productos, archivo_inventario)
    elif opcion == "2":
        inventario.registrar_venta(productos, archivo_ventas)
    elif opcion == "3":
        inventario.generar_reporte(productos)
    elif opcion == "4":
        inventario.generar_reporte_ventas(archivo_ventas)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Elija una opción válida por favor.")