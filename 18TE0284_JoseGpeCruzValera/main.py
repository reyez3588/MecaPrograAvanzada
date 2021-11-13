import Gerente
import empleado as emp
import wearing as ropa


def main():
    print("Bienvenido al programa de gestión de personal")
    print("¿Qué desea hacer?")
    print("[1] conocer el jefe")
    print("[2] verte al espejo")
    print("[3] conocer el número de empleados")
    print("[4] conocer la empresa")

    opcion = int(input("Introduzca una opción: "))

    if opcion == 1:
        Jefe_empresa = Gerente.boss("Rodrigo",43,25000,True)





