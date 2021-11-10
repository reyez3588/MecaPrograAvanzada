"""necesitamos empezar a modificar y crear la base del jefe"""

class ropa:
    def __init__(self, color:str, talla:str, marca:str, genero:str="Mujer"):
        self.__color = color
        self.__talla = talla
        self.__marca = marca
        self.__genero = genero

    def saco(self, botones:int=0):
        print("Saco de {} de {} de {}".format(self.color, self.talla, self.marca))
        print("Botones: {}".format(botones))

    def pantalon(self):
        print("Pantalon de {} de {}".format(self.color, self.marca))
        print("Talla: {}".format(self.__talla))

    def camisa(self, genero=None):
        print("Camisa de {} de {}".format(self.color, self.marca))
        print("Genero: {}".format(genero))

    def zapatos(self, marca=None):
        print("Zapatos de {} de {}".format(self.color, self.marca))
        print("Marca: {}".format(marca))




    def getterInfo(self):
        print ("Color: {}\nTalla: {}\nMarca: {}\nGenero: {}".format(self.__color, self.__talla, self.__marca, self.__genero))



    def __del__(self):
        print("Se ha eliminado la clase")








class hombre(ropa):
    def __init__(self, color:str, talla:str, marca:str, genero:str="Hombre"):
        super().__init__(color, talla, marca, genero)

    