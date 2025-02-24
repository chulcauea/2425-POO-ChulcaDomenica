import os

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

    # Método para representar un Producto como una línea en el archivo
    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"

    # Método para crear un Producto a partir de una línea del archivo
    @classmethod
    def desde_linea(cls, linea):
        datos = linea.strip().split(',')
        return cls(int(datos[0]), datos[1], int(datos[2]), float(datos[3]))

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Cargar el inventario desde el archivo."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as archivo:
                    for linea in archivo:
                        producto = Producto.desde_linea(linea)
                        self.productos.append(producto)
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al leer el archivo: {e}")
        else:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo.")

    def guardar_inventario(self):
        """Guardar los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as archivo:
                for producto in self.productos:
                    archivo.write(str(producto) + '\n')
            print("Inventario guardado correctamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el archivo: {e}")

    def agregar_producto(self, producto):
        """Agregar un producto al inventario y al archivo."""
        if self.buscar_producto_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto agregado correctamente.")
        else:
            print("Error: Ya existe un producto con ese ID.")

    def eliminar_producto(self, id):
        """Eliminar un producto del inventario y del archivo."""
        producto = self.buscar_producto_por_id(id)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print("Producto eliminado correctamente.")
        else:
            print("Error: No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualizar un producto en el inventario y en el archivo."""
        producto = self.buscar_producto_por_id(id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print("Producto actualizado correctamente.")
        else:
            print("Error: No se encontró ningún producto con ese ID.")

    def buscar_producto_por_id(self, id):
        """Buscar un producto por su ID."""
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        """Buscar productos por su nombre."""
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        """Mostrar todos los productos del inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

# Interfaz de usuario en la consola
def menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar inventario")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
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
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Por favor, ingrese valores numéricos para ID, cantidad y precio.")

if __name__ == '__main__':
    main()
