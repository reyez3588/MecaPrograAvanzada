#utilizando listas y diccionarios con csv para leer y escribir archivos
import csv
def generar_archivo():
    empleados = [
    ['Nombre', 'Apellido', 'Edad', 'Sexo', 'Puesto', 'Sueldo Mensual'],
    ['Juan', 'Perez', '23', 'M', 'Programador', '$14,000'],
    ['Maria', 'Gonzalez', '28', 'F', 'Jr Analisty coding', '$12,000'],
    ['Pedro', 'Gomez', '33', 'M', 'Lead Software Desing', '$14,000'],
    ['Ana', 'Rodriguez', '18', 'F', 'Lead Recursos Humanos', '$30,000'],
    ['Juana', 'Lopez', '27', 'F', 'Jefe de limpieza', '$7,000'],
    ['Luis', 'Gonzalez', '32', 'M', 'Programador', '$15,000'],
    ['Jorge', 'Gomez', '25', 'M', 'Evaluador de proyectos', '$10,000'],
    ['Maria', 'Perez', '22', 'F', 'Jefatura de innovacion', '$10,000'],
    ]
    # Escribir el archivo
    with open('personas.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(empleados)
        csvfile.close()
generar_archivo()

lista = []
class nomina:
    def __init__(self, nombre, apellido, edad, sexo, puesto, sueldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__sexo = sexo
        self.__puesto = puesto
        self.__sueldo = sueldo
    def getPuesto(self):
        return self.__puesto
    def getNombre(self):
        return self.__nombre

with open('personas.csv') as csvfile:
    puestos = csv.DictReader(csvfile)
    for filas in puestos:
        auxPersonal = nomina(filas['Nombre'], filas['Apellido'], filas['Edad'], filas['Sexo'], filas['Puesto'], filas['Sueldo Mensual'])
        lista.append(auxPersonal)
    csvfile.close()

def listaconsulta():
    for filas in lista:
        print('Nombre   :',filas.getNombre(),'  Puesto:',filas.getPuesto())
        