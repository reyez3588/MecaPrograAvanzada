"""realizare un programa de un jefe que pueda entrevistar a un empleado y conocer su nivel de ingles"""
import Vestimenta as Clothes
class persona():
    def __init__(self, name:str , age: int, pay:float, ropa:bool, nivel_ingles:int, altura:float):
        self,__altura = altura
        self.__name = str(name)
        self.__age = int(age)
        self.__pay = float(pay)
        self.__nivel = int(nivel_ingles)  # nivel de ingles superiores a 70 para aceptar
        self.__nivel_ingles = "nivel alto"
        self.__vestimenta = bool(ropa)
    try:
        name = property(lambda self: self.__name)
        age = property(lambda self: self.__age)
        pay = property(lambda self: self.__pay)
        nivel = property(lambda self: self.__nivel)
    except ValueError:
        print("error datos erroneos")
    except TypeError:
        print("error tipo de datos erroneos")
    except Exception:
        print("error desconocido")

    def get_name(self):
        return self.__name
    def get_invitacion(self): # invitacion de empleado a entrevistar
        #es como un get altura con la condicion de ser una entrevista y conocer la altura
        print("invitacion de entrevista de empleo")
        print('\n Correo recibido:\n'
        'Es de mi agrado informar que se ha agenda su cita con nuestro CEO')
        print(" El señor ",self.__name,'Es una gran empresario, mide ',self.__altura,
        'de altura')
        print("Posee un porte formal por lo que se le recomienda ")

class Gerente(persona):
    def __init__(self, name:str , age: int, pay:float, ropa:bool, nivel_ingles:int, altura:float):
        super().__init__(name, age, ropa, nivel_ingles, altura)
        self.__nivel_ingles = "nivel alto"
        self.__vestimenta = ropa
        if bool(ropa) == True:
            Gerente.__vestimenta()
        else:
            print("no se puso atension en la vestimenta")

    def saludo(self):
        print("hola soy el jefe, mi nombre es", self.__name, "y tengo", self.__age, "años")
        print("mi sueldo es de", self.__pay, "euros")
        print("mi nivel de ingles es", self.__nivel_ingles)

    def verVestimenta(self):
        pantalonGerente = Clothes.pantalon("Gris",'40','LV','Hombre')
        zapatosGerente = Clothes.zapatos("Negros","27","Flexi","Masculino")
        sacoGerente = Clothes.saco('Azul','Mediana','Rey Palomo','Hombre','Varias telas finas',3)
        camisetaGerente = Clothes.camiseta('azul','Large','Lacoste')
        # print()
        self.__verVestimenta(self)
        # camisetaGerente.getterInfo()
        camisetaGerente.verCAMISA()
        print()
        pantalonGerente.verPANTALON()
        print()
        sacoGerente.verSACO()
        print()

    def contrato(self):
        print("mi contrato es de", self.__pay, "euros")

    def others(self):
        pass

