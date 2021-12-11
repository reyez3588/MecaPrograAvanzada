import empleado as emp
import time
def presentacion():
    print ("Bienvenido al programa de empleados")
    print ("Escucha con atencion, no te olvides de tu contraseña cuando trabajes aqui 😉")
    print (
    '''
    Tu con nosostros tendras una mejor experiencia,
    porque te ayudaremos a que puedas administrar tus tiempos de forma eficiente.
    Necesitamos gente ampliamentes capacitada para que puedas entender nuestra empresa.
    Nuestra empresa es multinacional en el desarrollo de software
    y en el desarrollo de aplicaciones para dispositivos móviles.
    Nuestra empresa posee jóvenes profesionales con una amplia experiencia en el desarrollo de software.
    Tu puedes ser uno de ellos.
    Antes de empezar, te pediremos que nos cuentes un poco sobre ti.
    y te enviaremos un correo de bienvenida. con tu cita con directamente con nuestro CEO.



    Este mensaje esperemos te sea de ayuda. Y que pronto te veamos en nuestra empresa.
    Hasta la proxima. 😉
    '''
    )

def wellcome():
    print ("Bienvenido ", emp.get_Nombre(), " ", emp.get_Apellido())
    print ("Tu sueldo es de ", emp.get_Sueldo())
    print ('Ahora te encuentras asegurado')
    print ('Gracias por confiar en nosotros')
#Utilizando tuplas por que son inmutables y mas rapido
CEEOO = (
'Hola, ¿Cómo te llamas?',
'¿Algun otro nombre?',
'¿Cuál es tu apellido?',
'¿Cuál es tu sueldo que piensas aspirar aqui en esta ?',
'¿Cuál es tu número de seguro social?',
'De acuerdo vamos a comenzar',
'¿Cual es tu rama de estudio?',
'¿Posees titulo profesional con su cedula?',
'¿Que podrias aportar a esta empresa?',
'¿Te encuentras en la situacion desarrollar un proyecto con 3 personas mas que harias?',
'¿Por que debo de calificarte a este puesto?',
'Estas Dispuesto a aceptar 4000 mx',
'**Pensando',
'Quedas Contratrado Bienvenido a MedioMelon SA de CV')



Answer = (
'Ibai',
'Llanos',
'Treviño',
'$8000 mxn mensuales por ser mi primer empleo',
'123456789',
'De acuerdo',
'Ingeniería en Mecatronica',
'Titulo profesional y estoy tramitanto mi cedula mañana',
'Puedo ayudar a la empresa con el desarrollo de software de manera eficiente',
'Si, estoy en la situacion de desarrollar la comunicacion me enfocaria para desarrollarnos y desempenarnos mejor ',
'Porque soy una gran herramiento que siempre resuleve sus situaciones pese a sus condiciones',
'Si, estoy dispuesto a aceptar esos 4000 mx extra',
'**Nerviso',
'Muchas gracias CEO no desepcionare a  MedioMelon SA de CV'
)

def entrevistaCEO():

    for i in range(0,len(CEEOO)):
        print ("Ceo : ",CEEOO[i])
        time.sleep(0.5)
        print("Ibai : ",Answer[i])
        time.sleep(1)
        print('\n')

# entrevistaCEO()
# presentacion()
# wellcome()