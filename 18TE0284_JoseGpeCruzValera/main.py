import Gerente as Ceo
import empleado as emp
import Vestimenta as Clothes


def main():
    print("Bienvenido al programa de gestión de personal")
    print("¿Qué desea hacer?")
    print("[1] conocer el jefe")
    print("[2] verte al espejo")
    print("[3] conocer el número de empleados")
    print("[4] conocer la empresa")

    opcion = int(input("Introduzca una opción: "))

    if opcion == 1:
        CEO = Ceo.Gerente('Jose',45,25000,True,85,1.8)
        CEO.saludo()
        CEO.verVestimenta()
    try:
        opcion = int(input("Introduzca una opción: "))
    except ValueError:
        print("Introduzca un número")
main()