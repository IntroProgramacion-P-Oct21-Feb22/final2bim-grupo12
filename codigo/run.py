"""
    Proyecto Bimestral
    Segundo Bimestre
"""


def crearFacebook():
    """
    Método para cuenta de Facebook.

    Pregunta por nombre de usuario, edad, ciudad,
    pais, correo.

    Arma la cadena para retornarla al método principal.
    """
    print("Creando cuenta de Facebook\n")
    nombre = input("Ingrese su Nombre de Usuario\n")
    edad = int(input("Ingrese su Edad\n"))
    ciudad = input("Ingrese su Ciudad\n")
    pais = input("Ingrese su País\n")
    correo = input("Ingrese su Correo Electrónico\n")
    cadena = ("Nombre de Usuario: %s\n Edad: %d\n Ciudad: %s\n País: %s\n " 
              "Correo Electrónico: %s\n " % (nombre, edad, ciudad, pais, correo))
    return cadena


def crearTwitter():
    """
    Método para crear cuenta de Twitter.

    Pregunta por nombre de usuario, edad, ciudad
    pais, nombres, apellidos, correo.

    Directamente en el mismo se presenta en pantalla
    los datos ingresados, ya que no devuelve datos.
    """
    print("Creando cuenta de Twitter\n")
    nombre = input("Ingrese su Nombre de Usuario\n")
    edad = int(input("Ingrese su Edad\n"))
    ciudad = input("Ingrese su Ciudad\n")
    pais = input("Ingrese su País\n")
    nombres = input("Ingrese sus Nombres completos\n")
    apellidos = input("Ingrese sus Apellidos completos\n")
    correo = input("Ingrese su Correo Electrónico\n")
    print("Nombre de Usuario: %s\n Edad: %d\n Ciudad: %s\n País: %s\n " \
          "Nombres: %s\n Apellidos: %s\n Correo Electrónico: %s\n "
          % (nombre, edad, ciudad, pais, nombres, apellidos, correo))


def crearWhatsapp():
    """
    Método para crear cuenta de whatsapp.

    Pregunta por nombre de usuario, número de teléfono, edad ciudad
    y país.

    Almacena los datos ingresados en una variable cadena y es regresada
    a la función principal.
    """
    print("Creando cuenta de Whatsapp\n")
    nombre = input("Ingrese su Nombre de Usuario\n")
    telefono = int(input("Ingrese su Número de Teléfono\n"))
    edad = int(input("Ingrese su Edad\n"))
    ciudad = input("Ingrese su Ciudad\n")
    pais = input("Ingrese su País\n")

    cadena = ("Nombre de Usuario: %s\n Número de Teléfono: %d\n Edad: %d\n Ciudad: %s\n País: %s\n "
          % (nombre, telefono, edad, ciudad, pais ))
    return cadena


def crearTelegram():
    """
    Método para crear cuenta de Telegram

    Pregunta por nombre de usuario, número de teléfono, ciudad, país, área de interés.

    Se imprime directamente los datos ingresados, ya que no devuelve datos.
    """
    print("Creando cuenta de Telegram\n")
    nombre = input("Ingrese su Nombre de Usuario\n")
    telefono = int(input("Ingrese su Número de Teléfono"))
    ciudad = input("Ingrese su Ciudad\n")
    pais = input("Ingrese su País\n")
    area = input("Ingrese su Área de interés\n")
    print("Nombre de Usuario: %s\n Número de Teléfono: %d\n Ciudad: %s\n País: %s\n Área de Interés: %s\n"
              % (nombre, telefono, ciudad, pais, area))


def crearSignal():
    """
    Método para crear cuenta de Signal.

    Pregunta por nombre de usuario, ciudad, edad, hobby principal.

    Los arma en una variable cadena y devuelve esta al método principal.
    """
    print("Creando cuenta de Signal\n")
    nombre = input("Ingrese su Nombre de Usuario\n")
    ciudad = input("Ingrese su Ciudad\n")
    edad = int(input("Ingrese su Edad"))
    hobby = input("Ingrese su Correo Electrónico\n")
    cadena = ("Nombre de Usuario: %s\n Ciudad: %s\n Edad: %d\n Hobby Principal: %s\n"
              % (nombre, ciudad, edad, hobby))
    return cadena


def crearInstagram():
    """
    Método para crear cuenta de Instagram.

    Pregunta por nombre de usuario, ciudad, país, correo electrónico.

    Los datos son impresos directamente, ya que no queremos devolver una variable.
    """
    print("Creando cuenta de Instagram\n")
    nombre = input("Ingrese su Nombre de Usuario\n")
    ciudad = input("Ingrese su Ciudad\n")
    pais = input("Ingrese su Edad")
    correo = input("Ingrese su Correo Electrónico\n")
    print("Nombre de Usuario: %s\n Ciudad: %s\n País: %s\n Correo Electrónico: %s\n"
              % (nombre, ciudad, pais, correo))


def crearFlickr():
    """
    Método para crear cuenta de Flickr

    Pregunta por nombre de usuario, correo electrónico.

    Los arma en una cadena y devuelve esta variable al método principal.
    """
    print("Creando cuenta de Flickr\n")
    nombre = input("Ingrese su Nombre de Usuario\n")
    correo = input("Ingrese su Correo Electrónico\n")
    cadena = ("Nombre de Usuario: %s\n Correo Electrónico: %s\n"
          % (nombre, correo))
    return cadena


def obtenerMensaje(a):
    """
    Método para obtener el mensaje final

    Es llamada después de salir del ciclo y sirve para demostrar la
    afluencia de la campaña según el número de cuentas creadas.

    No queremos que devuelva el mensaje así que directamente se escribe el resultado
    desde este método.
    """
    mensajeFinal = (["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"])
    if a > 0 & a < 6:
        print(mensajeFinal[0])
    else:
        if a > 5 & a < 16:
            print(mensajeFinal[1])
        else:
            if a > 15:
                print(mensajeFinal[2])


cuentas = 0
confirma = "si"
while confirma != "no":
    cuentas = cuentas + 1
    numero = int(input("Ingrese 1-Facebook, 2-Twitter,"
                       " 3-Whatsapp, 4-Telegram,"
                       " 5-Signal, 6-Instagram, 7-Flickr\n"))
    if numero < 1 | numero > 7:
        print("Error en opción seleccionada")
    else:
        if numero == 1:
            facebook = crearFacebook()
            print(facebook)
        else:
            if numero == 2:
                crearTwitter()
            else:
                if numero == 3:
                    whatsapp = crearWhatsapp()
                    print(whatsapp)
                else:
                    if numero == 4:
                        crearTelegram()
                    else:
                        if numero == 5:
                            signal = crearSignal()
                            print(signal)
                        else:
                            if numero == 6:
                                crearInstagram()
                            else:
                                if numero == 7:
                                    flickr = crearFlickr()
                                    print(flickr)
    confirma = input("Si desea seguir añadiendo cuentas ingrese (si), caso contrario ingrese (no)\n")
obtenerMensaje(cuentas)
