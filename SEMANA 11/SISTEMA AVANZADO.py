import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["cantidad"], datos["precio"])

class Inventario:
    def __init__(self):
        self.productos = []

    def cargar_inventario(self, archivo="Inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                # Convertir cada diccionario a una instancia de Producto
                self.productos = [Producto.desde_diccionario(prod) for prod in datos]
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            self.productos = []
        except json.JSONDecodeError:
            print("Error al leer el archivo del inventario. Asegúrese de que el formato sea correcto.")
            self.productos = []

    def guardar_inventario(self, archivo="Inventario.json"):
        try:
            # Convertir cada producto a diccionario antes de guardar
            productos_dict = [producto.a_diccionario() for producto in self.productos]
            with open(archivo, "w") as f:
                json.dump(productos_dict, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if self.buscar_producto_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            print("Producto agregado correctamente.")
        else:
            print("Error: Ya existe un producto con ese ID.")

    def eliminar_producto(self, id):
        producto = self.buscar_producto_por_id(id)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Error: No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: No se encontró ningún producto con ese ID.")

    def buscar_producto_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

# Interfaz de usuario en la consola
inventario = Inventario()

# Cargar inventario al iniciar
inventario.cargar_inventario()

while True:
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar inventario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == '1':
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (o Enter para omitir): ")
            precio = input("Nuevo precio (o Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == '4':
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_productos_por_nombre(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for producto in resultados:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            inventario.guardar_inventario()  # Guardar inventario antes de salir
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos para ID, cantidad y precio.")

