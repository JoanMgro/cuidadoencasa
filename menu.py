from getpass import getpass

def menu_login():
    user = input('Ingrese Usuario: ')
    password = getpass('Ingrese password: ')

    return (user, password)


def menu_general_admon():
    print('Ingresar Nuevo')
    print('Actualizar Datos')
    print('Consultar Datos')
    print('Suspender Datos')
    print()
    opcion = input('Ingresar opcion: ', end="")

def menu_usuario():
    print('Ingresar signos vitales (Opcion 1):')
    print('Consultar historial (Opcion 2):')
    print()
    opcion = input('Ingresar opcion: ', end="")

def menu_medico():
    print('Consultar Datos Paciente (Opcion 1):')
    print('Consultar Sugerencias (Opcion 2):')
    print('Consultar Signos vitales (Opcion 3):')
    print()
    opcion = input('Ingresar opcion: ', end="")

def menu_ingresar_nuevo():

    print('Ingresar Nuevo Paciente (opcion 1): ')
    print('Ingresar Nuevo Medico (opcion 2): ')
    print()
    opcion = input('Ingresar opcion: ', end="")

def menu_actualizar_datos():
    print('Actualizar Datos Paciente (opcion 3): ')
    print('Actualizar Datos Medico (opcion 4): ')
    print()
    opcion = input('Ingresar opcion: ', end="")


def menu_consultas_datos():
    print('Consultar Paciente(opcion 5): ')
    print('Consultar Medico (opcion 6): ')
    print()
    opcion = input('Ingresar opcion: ', end="")

def menu_suspender():
    print('Eliminar Paciente(opcion 7): ')
    print('Eliminar Medico (opcion 8): ')
    print()
    opcion = input('Ingresar opcion: ', end="")




def menu_ingresar_signos():
    pass














