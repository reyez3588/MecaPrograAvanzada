"""Se realizara una clase de empleado para poder entrevistarlo"""
#aplicamos encapsulamiento
#como tambien privado y publico de ciertos argumentos
class Empleado():
    def __init__(self, nombre, apellido, edad, salario, nivel_ingles):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__salario = salario
        self.__nivel_ingles = nivel_ingles

    def get_nombre(self):
        return self.__nombre
    def entrevista(self):
        print("Hola, mi nombre es {} {} y tengo {} años".format(self.__nombre, self.__apellido, self.__edad))
        print("Mi salario es de {} y mi nivel de ingles es de {}".format(self.__salario, self.__nivel_ingles))

    def celebracion(self, acuerdo=True):
        if acuerdo == "si" or "Si" or "SI":
            aceptacion = True
        if aceptacion == True:
            print("Estoy de acuerdo con el contrato, {} {}".format(self.__nombre, self.__apellido))
        else:
            print("Lo siento, {} {}".format(self.__nombre, self.__apellido))
        print("Acepto el contratro")