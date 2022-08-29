import menu



def main():
    datos_usuario = menu.menu_login()
    #autenticar entrada con db.
    #si ok sigue a menu entrada:
    tipo_usuario = 1 #el tipo lo debe retornar la db.
    opcion = menu.menu_entrada(tipo_usuario)
    menu.menu_operaciones(tipo_usuario, opcion)
    












if __name__ == '__main__':
    main()





