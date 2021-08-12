import getpass
import time

def lobby():
    print("1) Iniciar sesion")
    print("2) Registrarse")
    print("3) Salir")

def lobbyio(userInput):
    try:
        userInput=int(userInput)
        if(1<=userInput<=3):
            return 1
        else:
            print('opcion invalida')
            time.sleep(1)
            return 0
    except:
        print('opcion invalida')
        time.sleep(1)
        return 0

def homeio(userInput):
    try:
        userInput=int(userInput)
        if(1<=userInput<=69):
            return 1
        else:
            print('opcion invalida')
            time.sleep(1)
            return 0
    except:
        print('opcion invalida')
        time.sleep(1)
        return 0

def iniciosesion():
    print("--  Inicio de Sesion  --")
    user=input("entrar usuario: ")
    password=getpass.getpass("Contraseña: ")
    return user,password

def agregar():
    while 1:
        print("--  agregar contacto  --")
        user=input("usuario: ")
 
        if('@' not in user):
            print('no se especifico servidor')
        else:
            return user

        time.sleep(2)
        

def busqueda():
    while 1:
        print("--  Busqueda de usuario  --")
        user=input("usuario (especificar servidor): ")
 
        if('@' not in user):
            print('no se especifico servidor')
        else:
            return user

        time.sleep(2)
        


def mostrartodos():
    print("--  Usuarios conectados  --")

def contactos():
    print("--  Lista de contactos  --")


def menuprincipal(notification=None):
    print("--  Menu Principal  --")
    print()
    if(notification):
        print(u"\u001b[1m\u001b[31m●\u001b[0m "+notification)
    else:
        print("")
    print("")
    print("1) Mostar todos los usuarios")
    print("2) Agregar contacto")
    print("3) Buscar usuario")
    print("4) buzon")
    print("5) Cambio de estado")
    print("6) Eliminacion de cuenta")
    print("7) Exit")

def chatprivado(user):
    user=user[:user.find('@')]
    
    print("--  Chat con "+user+"  --")

def estado():
    status={
        1:'available',
        2:'away',
        3:'dnd',
        4:'xa',
    }
    while 1:
        print("--  Cambio de estado  --")
        print("1) Disponible")
        print("2) AFK")
        print("3. Ocupado")
        print("4. AFK prolongado")
        statusIndex=input("Ingrese opcion: ")

        try:
            if(1<=int(statusIndex)<=4):
                presence=input('cambia tu mensaje de presencia: ')
                return status[int(statusIndex)],presence
            else:
                print('opcion invalida')
                time.sleep(2)
                
                continue
        except:
            print('Ingresa el numero de tu opcion')

        time.sleep(2)
        


def buzon(contacts):
    while 1:
        print("--  Buzon privado  --")
        for i in range(len(contacts)):
            if(contacts[i][1]):
                print(f"{i+1}. {contacts[i][0]}"+u"\u001b[1m\u001b[31m ●\u001b[0m")
            else:
                print(f"{i+1}. {contacts[i][0]}")

        print(f"{len(contacts)+1}. Enviar mensaje privado")
        print(f"{len(contacts)+2}. Salir")

        userInput=input("Ingresar opcion: ")

        try:
            print(userInput)
            if(1<=int(userInput)<=len(contacts)+2):
                print('---')
                if(int(userInput)==len(contacts)+2):
                    return -100, False
                if(int(userInput)==len(contacts)+1):
                    usuario=input('Destinatario(xxx@yy): ')
                    return usuario, True
                return contacts[int(userInput)-1][0], False
            else:
                print('opcion invalida')
        except:
            print('ingresa el numero correspondiente a tu opcion')

        time.sleep(2)
        

def registro():
    while 1:
        print("--  Registro  --")
        user=input("Usuario: ")
        password=getpass.getpass("Contraseña: ")
        confirmPassword=getpass.getpass("Confirmar contraseña: ")
        if('@' not in user):
            print('No se especificó servidor')
        if(password != confirmPassword):
            print('Las contraseñas no coinciden')
        if(('@' in user) and (password==confirmPassword)):
            return user,password

        print(user)
        print(password)
        print(confirmPassword)
        time.sleep(2)
        
