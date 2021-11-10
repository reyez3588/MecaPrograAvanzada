"""realizare un programa de un jefe que pueda entrevistar a un empleado y conocer su nivel de ingles"""

class boss:
    def __init__(self, name:str , age: int, pay:float, ropa:str, nivel_ingles:int):
        self.__name = str(name)
        self.__age = int(age)
        self.__pay = float(pay)
        self.__nivel = int(nivel_ingles)  # nivel de ingles superiores a 70 para aceptar
        self.__nivel_ingles = "nivel alto"
        self.__vestimenta = str(ropa)
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

    def saludo(self):
        print("hola soy el jefe, mi nombre es", self.__name, "y tengo", self.__age, "años")
        print("mi sueldo es de", self.__pay, "euros")
        print("mi nivel de ingles es", self.__nivel_ingles)

    def vestimenta(self):
        print("mi vestimenta es", self.__vestimenta)

    def contrato(self):
        print("mi contrato es de", self.__pay, "euros")

    def others(self):
        pass