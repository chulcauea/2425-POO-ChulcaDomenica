# Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos comunes a todos los animales
        self.nombre = nombre
        self.edad = edad

    # Método que describe cómo un animal emite un sonido, sobrescrito en clases derivadas
    def hacer_sonido(self):
        raise NotImplementedError("El método hacer_sonido debe ser sobrescrito por las clases derivadas")

    # Método para obtener la información básica del animal
    def obtener_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad} años"


# Clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Inicializa atributos de la clase base Animal
        super().__init__(nombre, edad)
        # Atributo específico de Perro
        self.raza = raza

    # Sobrescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"

    # Método específico para obtener la raza del perro
    def obtener_raza(self):
        return f"La raza de {self.nombre} es {self.raza}"


# Clase derivada Gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Inicializa atributos de la clase base Animal
        super().__init__(nombre, edad)
        # Atributo específico de Gato
        self.__color = color  # Atributo privado (Encapsulación)

    # Sobrescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"

    # Método getter para obtener el color del gato
    def obtener_color(self):
        return self.__color


# Función principal
def main():
    # Crear instancias de Perro y Gato
    perro1 = Perro("Lucas", 2, "Pastor Aleman")
    gato1 = Gato("Figaro", 3, "Plomo")

    # Mostrar información de los animales y los sonidos que hacen
    print(perro1.obtener_info())  # Información del perro
    print(perro1.hacer_sonido())  # Sonido del perro

    print(gato1.obtener_info())   # Información del gato
    print(gato1.hacer_sonido())   # Sonido del gato

    # Acceder al atributo privado __color del gato mediante el método getter
    print(gato1.obtener_color())  # Color del gato

    # Mostrar información específica de la raza del perro
    print(perro1.obtener_raza())  # Raza del perro


if __name__ == "__main__":
    main()
