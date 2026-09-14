# Gestion-inventario-y-ventas-Munive-VillalbaS

Aquí tienes un ejemplo de **README.md** para tu proyecto de inventario y ventas en consola con Python. Lo redacté en un estilo claro y amigable, como se suele usar en proyectos de hobby o aprendizaje:

---

```markdown
# 📦 Sistema de Inventario y Ventas en Python

Este proyecto es un sistema de consola escrito en **Python** que permite gestionar un inventario de productos y registrar ventas de manera sencilla.  
Se diseñó como práctica de programación modular, manejo de archivos y estructuras de datos (listas y diccionarios).

---

## 🚀 Funcionalidades

- **Alta de producto**: agregar nuevos productos al inventario con código, nombre, categoría, precio y stock.
- **Registro de venta**: descontar stock y guardar la transacción en un archivo de ventas.
- **Reporte de inventario**: mostrar todos los productos, su stock y el valor total del inventario.
- **Reporte de ventas**: mostrar todas las ventas registradas y el total acumulado.
- **Persistencia en archivos**:
  - `inventario.txt` → almacena los productos.
  - `ventas.txt` → almacena las ventas.

---

## 🧩 Estructura del proyecto

```
inventario.py   # Funciones para manejar productos y ventas
menu.py         # Menú interactivo en consola
principal.py    # Programa principal que une todo
inventario.txt  # Archivo de datos del inventario
ventas.txt      # Archivo de datos de ventas
```

---

## 📖 Uso

1. Clona o descarga este repositorio.
2. Asegúrate de tener **Python 3.x** instalado.
3. Ejecuta el programa principal:

```bash
python principal.py
```

4. Usa el menú para:
   - Opción 1 → Alta de producto (se guarda en `inventario.txt`).
   - Opción 2 → Registrar venta (se guarda en `ventas.txt`).
   - Opción 3 → Generar reporte de inventario.
   - Opción 4 → Generar reporte de ventas.
   - Opción 5 → Salir.

---

## 📂 Ejemplo de archivos generados

**inventario.txt**
```
P001,Manzana,Fruta,2.5,10
P002,Pan,Panadería,1.0,20
```

**ventas.txt**
```
P001,2,5.0
P002,1,1.0
```

---

## 🎯 Objetivo del proyecto

Este sistema busca:
- Practicar programación modular en Python.
- Aprender manejo de archivos (`open`, `read`, `write`, `append`).
- Usar estructuras de datos eficientes (listas y diccionarios).
- Aplicar validaciones y manejo de excepciones.

---

## 🛠️ Mejoras futuras

- Búsqueda de productos por nombre o categoría.
- Exportar reportes a CSV o PDF.
- Interfaz gráfica simple con Tkinter o PyQt.
- Integración con bases de datos (SQLite o MySQL).

---

## 👨‍💻 Autor

Proyecto creado por **José Munive Guerra y Carlos Villalba Santos** como práctica de programación en Python.
```
