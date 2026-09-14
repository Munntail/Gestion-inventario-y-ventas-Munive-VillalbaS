# -------------------------------
# Aqui tenemos todas nuestras funciones para usar en el principal
# -------------------------------

# -------------------------------
# Para cargar los datos en el archivero
# -------------------------------
def cargar_datos(nombre_archivo):
    inventario = {}
    try:
        with open(nombre_archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 5:
                    codigo, nombre, categoria, precio, stock = partes
                    inventario[codigo] = {
                        "nombre": nombre,
                        "categoria": categoria,
                        "precio": float(precio),
                        "stock": int(stock)
                    }
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo al guardar.")
    
    return inventario


# -------------------------------
# Para guardar SOLO un producto nuevo en el archivero (append)
# -------------------------------
def guardar_producto(nombre_archivo, codigo, datos):
    try:
        with open(nombre_archivo, "a") as f:
            linea = f"{codigo},{datos['nombre']},{datos['categoria']},{datos['precio']},{datos['stock']}\n"
            f.write(linea)
    except Exception:
        print("No se pudo guardar el producto")
    else:
        print(f"Producto {codigo} guardado correctamente.")


# -------------------------------
# Para dar alta al producto
# -------------------------------
def alta_producto(inventario, archivo):
    codigo = input("Ingrese código del producto: ").strip().upper()
    if codigo in inventario:
        print("Ese código ya existe.")
        return
    
    nombre = input("Ingrese nombre: ").strip()
    categoria = input("Ingrese categoría: ").strip()
    
    try:
        precio = float(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))
        if precio < 0 or stock < 0:
            raise ValueError("Precio o stock no pueden ser negativos.")
    except ValueError:
        print("Error: Ingrese valores válidos")
        return
    
    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    print("Producto agregado exitosamente.")
    
    # Guardar directamente en archivo sin borrar lo anterior
    guardar_producto(archivo, codigo, inventario[codigo])


# -------------------------------
# Para registrar una venta y guardarla en archivo aparte
# -------------------------------
def registrar_venta(inventario, archivo_ventas):
    codigo = input("Ingrese código del producto vendido: ").strip().upper()
    if codigo not in inventario:
        print("Producto no encontrado.")
        return
    
    try:
        cantidad = int(input("Ingrese cantidad vendida: "))
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        if cantidad > inventario[codigo]["stock"]:
            print("Stock insuficiente.")
            return
    except ValueError:
        print("Error: Ingrese una cantidad numérica")
        return
    
    inventario[codigo]["stock"] -= cantidad
    total = inventario[codigo]["precio"] * cantidad
    print(f"Venta registrada. Stock actual de {codigo}: {inventario[codigo]['stock']}")
    
    # Guardar la venta en archivo de ventas
    try:
        with open(archivo_ventas, "a") as f:
            linea = f"{codigo},{cantidad},{total}\n"
            f.write(linea)
    except Exception:
        print("No se pudo guardar la venta")
    else:
        print("Venta guardada correctamente.")


# -------------------------------
# Función: Generar reporte de inventario
# -------------------------------
def generar_reporte(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    
    print("\nREPORTE DE INVENTARIO")
    print("=" * 50)
    total_valor = 0
    for codigo, datos in inventario.items():
        subtotal = datos["precio"] * datos["stock"]
        total_valor += subtotal
        print(f"{codigo} | {datos['nombre']} | {datos['categoria']} | Precio: {datos['precio']} | Stock: {datos['stock']} | Subtotal: {subtotal}")
    print("=" * 50)
    print(f"Valor total del inventario: {total_valor:.2f}")


# -------------------------------
# Función: Generar reporte de ventas
# -------------------------------
def generar_reporte_ventas(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            ventas = f.readlines()
    except FileNotFoundError:
        print("No hay archivo de ventas todavía.")
        return
    
    if not ventas:
        print("No hay ventas registradas.")
        return
    
    print("\nREPORTE DE VENTAS")
    print("=" * 50)
    total_general = 0
    for linea in ventas:
        codigo, cantidad, total = linea.strip().split(",")
        print(f"Producto: {codigo} | Cantidad: {cantidad} | Total: {total}")
        total_general += float(total)
    print("=" * 50)
    print(f"Total general de ventas: {total_general:.2f}")