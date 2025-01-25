class computer:

    # METODO CONSTRUCTOR
    def __init__(self,brand,capacity,ram):
        self.brand=brand
        self.capacity=capacity
        self.ram=ram
        print(f"Accedimos al constructor del pc")

    #METODO PERONALIZADO
    def imprimirinfopc(self):
        print(
            f"Soy la Computadora marca {self.brand} con almacenamiento de{self.capacity}GB y memoria de {self.ram} GB"
        )

    #METODO DESTRUCTOR
    def __del__(self):
        print(f"El metodo destructor se ah ejecutado")

mi_computadora=computer(brand="Hp",capacity=" 64",ram="8")
mi_computadora.imprimirinfopc()
