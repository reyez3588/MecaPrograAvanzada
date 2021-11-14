import Gerente as Ceo
import empleado as emp
import Vestimenta as Clothes
import time



CEOdEmpresar = Ceo.Gerente('Julio',45,39999.99,str(85),1.80)
pantalonGerente = Clothes.pantalon("Gris",'Mediana 34','LV','Hombre')
zapatosGerente = Clothes.zapatos("Negro","27","Flexi","Masculino")
sacoGerente = Clothes.saco('Azul','Mediana 36','Rey Palomo','Hombre','Varias telas finas',3)
camisetaGerente = Clothes.camiseta('azul','Mediana 34','Lacoste')





def main():
    Secretaria = Ceo.persona('Maria',25,1500.00,'b1',1.65)
    Secretaria.get_name()
    print("\nBienvenido al programa de gestión de personal")
    print("¿Qué desea hacer?")
    print("[1] conocer el jefe")
    print("[2] verte al espejo")
    print("[3] conocer el número de empleados")
    print("[4] conocer la empresa")
    print("[5] Empresar la entrevista")

    opcion = int(input("Introduzca una opción: "))


    if opcion == 1:
        print("\nEl jefe de la empresa es: ", CEOdEmpresar.get_name())
        camisetaGerente.verCAMISA()
        pantalonGerente.verPANTALON()
        sacoGerente.verSACO()
        zapatosGerente.verZAPATOS()
        # CEOdEmpresar.verGerente()
        # CEO.verVestimenta()
        time.sleep(3)
        return main()
        #-----------------------------------------------------s
    elif opcion == 2:
        pass

        time.sleep(3)
        return main()
        #-----------------------------------------------------
    elif opcion == 3:
        pass

        time.sleep(3)
        return main()
        #----------------------------------------------------------------------------------------------------------------
    elif opcion == 4:
        pass


        time.sleep(3)
        return main()
        #----------------------------------------------------------------------------------------------------------------
    elif opcion == 5:
        pass

        time.sleep(3)
        return main()
        #----------------------------------------------------------------------------------------------------------------
    elif opcion == 6:
        print("\nGracias por usar el programa")
        print('Cerrando programa ⏱️')
        print("\n3..")
        time.sleep(1)
        print("   2..")
        time.sleep(1)
        print("       1..")
        time.sleep(1)
        exit()
        #----------------------------------------------------------------------------------------------------------------

    # else:
    #     print("Opción incorrecta")
    #     return main()
    # try:
    #     opcion = int(input("Introduzca una opción: "))
    # except ValueError:
    #     print("EROR 404 reintente               \n")
    # except int.ValueError:
    #     print("Introduzca un número             \n\n\n\n\n")
    # except KeyboardInterrupt:
    #     print('Saliendo de programa')
    # finally:
    #     return main()

main()