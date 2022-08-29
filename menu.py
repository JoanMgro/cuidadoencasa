from getpass import getpass
import menuadmon


def menu_login():
    user = input('Ingrese Usuario: ')
    password = getpass('Ingrese password: ')

    return (user, password)


def menu_entrada(un_tipo_usuario):
    if un_tipo_usuario == 1:
        menuadmon.menu_general()
    elif un_tipo_usuario == 2:
        pass
    elif un_tipo_usuario == 3:
        pass

def menu_operaciones(un_tipo_usuario, una_opcion):

    if un_tipo_usuario == 1:
        if una_opcion == 1:
            menuadmon.menu_ingresar_nuevo()
        elif una_opcion == 2:
            menuadmon.menu_actualizar_datos()
        elif una_opcion == 3:
            menuadmon.menu_consultas_datos()
        elif una_opcion == 4:
            menuadmon.menu_suspender()
    elif un_tipo_usuario == 2:
        pass
    elif un_tipo_usuario == 3:
        pass








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



def menu_ingresar_signos():
    pass














