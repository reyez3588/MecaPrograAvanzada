import Gerente as Ceo
import Empleado as emp
import Vestimenta as Clothes
import time
import Assetstools as assets
#creamos el objeto CEO -------------------------------------------------
CEOdEmpresar = Ceo.Gerente('Jose Antonio Ponton',45,39999.99,str(85),1.80)
pantalonGerente = Clothes.pantalon("Gris",'Mediana 34','LV','Hombre')
zapatosGerente = Clothes.zapatos("Negro","27","Flexi","Masculino")
sacoGerente = Clothes.saco('Azul','Mediana 36','Rey Palomo','Hombre','Varias telas finas',3)
camisetaGerente = Clothes.camiseta('azul','Mediana 34','Lacoste')
#creamos su ropa de trabajo -------------------------------------------------
#       Pantalon
#           Camisa
#               Zapatos
#                   Saco con los 3 botones
#--------------------------------------------------------------------------------

# crearemos al emmpleado -------------------------------------------------
# vestiremos formalmente
Entrevistado = emp.Empleado(" Ricardo ",'Mendez Allende',22,15000,str(85),1.70)
pantalonEntrevistado = Clothes.pantalon("Gris",'Mediana 32','Oxfort','Hombre')
camisetaEntrevistado = Clothes.camiseta('Negra','Mediana 32','IDesign')

#----------------------------------------------------------------------------------------------------------------


#crearemos el obejeto Secretaria---------------------------------------------------------
Secretaria = Ceo.persona('Maria Buena Aventura',25,1500.00,'b1',1.65)
print(""" Hola buenas tardes mi nombre es {} le acabo de enviar un correo de la empresa para su 
    solicitud de empleo, en breves momentos le llegara...""".format(Secretaria.get_name()))
#----------------------------------------------------------------------------------------------------------------
assets.cargando()
CEOdEmpresar.get_invitacion()
print('Bienvenido al programa de Entrevista de trabajo')

def main():
    print("""\n\n
    ¿Qué desea hacer?
    [1] conocer el jefe
    [2] verte al espejo
    [3] conocer el número de empleados
    [4] conocer la empresa
    [5] Empresar la entrevista
    [6] Salir\n""")

    opcion = int(input("Introduzca una opción: "))


    if opcion == 1:
        print('Reconoceras Nuestro CEO con las siguientes caracteristicas comunes')
        print("\nEl jefe de la empresa es:    {}".format(CEOdEmpresar.get_name()))
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
        assets.cargando2()
        exit()
        #----------------------------------------------------------------------------------------------------------------
    else:
        print("\nEsa opción no existe")
        time.sleep(2)
        return main()
    # else:
    #     print("Opción incorrecta")
    #     return main()
    
    # except int.ValueError:
    #     print("Introduzca un número             \n\n\n\n\n")
    # except KeyboardInterrupt:
    #     print('Saliendo de programa')
    # finally:
    #     return main()




main()