import json

class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }
class Usuario:
    def __init__(self,id_usuario,nombre,libros_prestados=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = libros_prestados if libros_prestados is not None else []
    def to_dict(self):
        return{
            "id usuario": self.id_usuario,
            "nombre": self.nombre,
            "libros prestados": self.libros_prestados
        }

class Biblioteca:
    def __init__(self, archivo_libros='biblioteca.json', archivo_usuarios= 'usuarios.json' ):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.libros = self.cargar_datos(self.archivo_libros)
        self.usuarios = self.cargar_datos(self.archivo_usuarios)


    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_datos(self, archivo, datos):
        with open(archivo, 'w') as f:
            json.dump(datos, f , indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro.to_dict()
        self.guardar_datos(self.archivo_libros, self.libros)

    def registrar_usuario(self,usuario):
        self.usuarios[usuario.id_usuario] = usuario.to_dict()
        self.guardar_datos(self.archivo_usuarios, self.usuarios)

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros and not self.libros[isbn]["prestado"]:
            self.libros[isbn]["prestado"] = True
            self.usuarios[id_usuario]["libros prestados"].append(isbn)
            self.guardar_datos(self.archivo_libros, self.libros)
            self.guardar_datos(self.archivo_usuarios, self.usuarios)
            print(f"libro {isbn} prestado a {id_usuario}.")
        else:
            print("Libro no disponible para préstamo.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.usuarios[id_usuario]["libros prestados"]:
            self.usuarios[id_usuario]["libros prestados"].remove(isbn)
            self.libros[isbn]["prestado"] = False
            self.guardar_datos(self.archivo_libros, self.libros)
            self.guardar_datos(self.archivo_usuarios, self.usuarios)
            print(f"Libro {isbn} devuelto por {id_usuario}.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro["prestado"] else "Disponible"
            print(f"{libro['isbn']}: {libro['titulo']} por {libro['autor']} - {estado}")

    def mostrar_usuario(self):
        for usuario in self.usuarios.values():
            print(f"{usuario['id_usuario']}: {usuario['nombre']}, libros prestados: {usuario['loibros prestados']}")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Registrar Usuario\n3. Mostrar Libro\n4. Prestar Libro\n5. Devolver Libro\n6. Mostrar Usuario\n7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            isbn = input("codigo: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            id_usuario = input("ID Usuario:")
            nombre = input("Nombre:")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)
        elif opcion == '3':
            biblioteca.mostrar_libros()
        elif opcion == '4':
            id_usuario = input("ID Usuarios:")
            isbn = input("codigo del libro:")
            biblioteca.prestar_libro(id_usuario, isbn)
        elif opcion == '5':
            id_usuario = input("ID Usuarios:")
            isbn = input("codigo del libro:")
            biblioteca.devolver_libro(id_usuario, isbn)
        elif opcion == '6':
            biblioteca.mostrar_usuario()
        elif opcion == '7':
            print("Saliendo del Sistema....")
            break
        else:
            print("Opcion no valida. Intente de nuevo")

if __name__ == "__main__":
    menu()
