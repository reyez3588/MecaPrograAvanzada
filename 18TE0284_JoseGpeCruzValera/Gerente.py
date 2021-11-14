"""realizare un programa de un jefe que pueda entrevistar a un empleado y conocer su nivel de ingles"""
import Vestimenta as Clothes
class persona():
    def __init__(self, name:str , age: int, pay:float,nivel_ingles:str='A1', altura:float= 1.80):
        self.__altura = float(altura)
        self.__name = str(name)
        self.__age = int(age)
        self.__pay = float(pay)
        self.__nivel_ingles = str(nivel_ingles)
    try:
        print('Running...\n\n\n')
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
        print("Posee un porte formal por lo que se le recomienda")
        print('Necesitara manejar ingles %s'%self.__nivel_ingles)

class Gerente(persona):
    def __init__(self, name:str , age: int, pay:float, nivel_ingles:str = 'C1', altura:float=1.80):
        super().__init__(name, age, nivel_ingles, altura)

    def saludo(self):
        print("hola soy el jefe, mi nombre es", self.__name, "y tengo", self.__age, "años")
        print("mi sueldo es de", self.__pay, "euros")
        print("mi nivel de ingles es", self.__nivel_ingles)

    def contrato(self):
        print("mi contrato es de", self.__pay, "euros")

    def others(self):
        pass
    def getAltura(self):
        return self.__altura



#codigo de testeo no descomentar
    # def verVestimenta(self):
        # pantalonGerente = Clothes.pantalon("Gris",'40','LV','Hombre')
        # zapatosGerente = Clothes.zapatos("Negros","27","Flexi","Masculino")
        # sacoGerente = Clothes.saco('Azul','Mediana','Rey Palomo','Hombre','Varias telas finas',3)
        # camisetaGerente = Clothes.camiseta('azul','Large','Lacoste')
        # # print()
        # self.__verVestimenta(self)
        # # camisetaGerente.getterInfo()
        # camisetaGerente.verCAMISA()
        # print()
        # pantalonGerente.verPANTALON()
        # print()
        # sacoGerente.verSACO()
        # print()