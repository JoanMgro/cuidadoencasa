
def menu_general():
    print('Ingresar Nuevo')
    print('Actualizar Datos')
    print('Consultar Datos')
    print('Suspender Datos')
    print()
    while True:
        try:
            opcion = int(input('Ingresar opcion: ', end=""))
            break
        except ValueError:
            print('opcion incorrecta')
   
    

def menu_ingresar_nuevo():

    print('Ingresar Nuevo Paciente (opcion 1): ')
    print('Ingresar Nuevo Medico (opcion 2): ')
    print()
    while True:
        try:
            opcion = int(input('Ingresar opcion: ', end=""))
            break
        except ValueError:
            print('opcion incorrecta')

    if opcion == 1:
        pass
    elif opcion == 2:
        pass


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




