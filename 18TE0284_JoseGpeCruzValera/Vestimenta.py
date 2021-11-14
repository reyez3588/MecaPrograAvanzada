"""necesitamos empezar a modificar y crear la base del jefe"""
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                         -Armario principal-
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class ropa:
    def __init__(self, color:str, talla:str, marca:str, genero:str="Unisex"):
        self.__color = color
        self.__talla = talla
        self.__marca = marca
        self.__genero = genero

    def getterInfo(self):
        print ("Color: {}\nTalla: {}\nMarca: {}\nGenero: {}"
        .format(self.__color, self.__talla, self.__marca, self.__genero))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                            -SACO-
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class saco(ropa):
    def __init__(self, color:str, talla:str, marca:str,
                genero:str="Unisex", material:str="Formal",botones:int=0):
        super().__init__(color, talla, marca, genero)
        self.__color  = color
        self.__talla  = talla
        self.__marca  = marca
        self.__genero = genero
        self.__material = material
        self.__botones = botones
    def verSACO(self):
        print("Su Saco color {} de talla {}, Marca: {}".format(self.__color, self.__talla, self.__marca))
        print("Posee {} botone(s) su saco       ".format(self.__botones))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                            -Pantalon-
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class pantalon(ropa):
    def __init__(self, color:str, talla:str, marca:str,
                genero:str="Hombre"):
        super().__init__(color, talla, marca)
        self.__color = color
        self.__talla = talla
        self.__marca = marca
    def verPANTALON(self):
        print("Pantalon  {} de la {}, marca {}".format(self.__color, self.__talla, self.__marca))
        print("Talla    : {}".format(self.__talla))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                            -CAMISETA-
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class camiseta(ropa):
    def __init__(self, color:str, talla:str, marca:str,
                genero:str="Unisex"):
        super().__init__(color, talla, marca, genero)
        self.__color = color
        self.__talla = talla
        self.__marca = marca
        self.__genero = genero

    def verCAMISA(self):
        print("Camisa de {} de {}".format(self.__color, self.__marca))
        print("Su talla es aprox    : {}".format(self.__talla))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                            -Zapatos-
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class zapatos(ropa):
    def __init__(self, color:str, talla:str, marca:str,
                genero:str="Unisex"):
        super().__init__(color, talla, marca)
        self.__color = color
        self.__talla = talla
        self.__marca = marca
        self.__genero = genero
#------------------------------------------------------------------------------
    def verZAPATOS(self):
        print("Zapatos color:   {},\nMarca     {}".format(self.__color, self.__marca))
        print("Talla: {}".format(self.__talla))

# pantalonGerente = pantalon("Gris",'40','LV','Hombre')
# zapatosGerente = zapatos("Negros","27","Flexi","Masculino")
# sacoGerente = saco('Azul','Mediana','Rey Palomo','Hombre','Varias telas finas',3)
# camisetaGerente = camiseta('azul','Large','Lacoste')

# print()
# # camisetaGerente.getterInfo()
# camisetaGerente.verCAMISA()
# print()
# pantalonGerente.verPANTALON()
# print()
# sacoGerente.verSACO()
# print()

# pantalonGerente.getterInfo()
# zapatosGerente.getterInfo()