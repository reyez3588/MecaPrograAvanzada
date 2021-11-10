"""Se realizara una clase de empleado para poder entrevistarlo"""

class Empleado():
    def __init__(self, nombre, apellido, edad, salario, nivel_ingles):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.nivel_ingles = nivel_ingles
    def entrevista(self):
        print("Hola, mi nombre es {} {} y tengo {} años".format(self.nombre, self.apellido, self.edad))
        print("Mi salario es de {} y mi nivel de ingles es de {}".format(self.salario, self.nivel_ingles))