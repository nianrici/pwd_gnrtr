#!/bin/env python

"""
Título:     Generador casero de contraseñas
Creador:    Nicolas Riquelme
Fecha:      2022-08-31

TODO en nuevas versiones:
    - añadir validación de longitud min y max
"""

import string
import random
import time
import subprocess
import pyfiglet
from termcolor import colored
import pyperclip as cb


# creamos 2 listas con los caractéres que definirán la complejidad de la contraseña
TYPEA = string.ascii_letters + string.digits
TYPEB = string.ascii_letters + string.digits + string.punctuation

# generamos y pintamos el banner reshulón
banner = pyfiglet.figlet_format(" PWD\nGNRTR", font="poison")
banner = colored(banner, 'green', attrs=['blink'])
print(banner)

# generamos el mensaje de error y lo ponemos rojo para que destaque
MEC = "\nMala elección, elige A o B\n\n"
MEC = colored(MEC, 'red', attrs=['bold'])

MEC2 = "\nMala elección, elige s o n"
MEC2 = colored(MEC, 'red', attrs=['bold'])
# le preguntamos al usuario y comprobamos que la respuesta sea válida
while True:
    tipo = input("""
    Cómo de compleja ha de ser?
    \nSELECCIONA:
    \n    A: Sencilla (mayúsculas, minúsculas y números)
    \n    B: Compleja (como A, pero además con símbolos)
    \n""").strip().lower()
    if tipo not in ("a","b"):
        print(MEC)
    else:
        break

# le preguntamos por la longitud de la contraseña
veces = int(input("\nCuantos caracteres ha de tener?:\n"))

# creamos la variable que contendrá la contraseña generada vacía
PWD = ''

# creamos el contador a cero
i = 0

# generamos la mágia
while i != veces:
    if tipo == 'a':
        k = random.choice(TYPEA)
        PWD = PWD + k
        i = i + 1
    if tipo == 'b':
        k = random.choice(TYPEB)
        PWD = PWD + k
        i = i + 1

# copiamosla contraseña al portapapeles antes de pintarla
cb.copy(PWD)

# pintamos la contraseña
colPWD = colored(PWD, 'yellow', attrs=[])

# la mostramos al usuario
print("\nHe generado y copiado al portapapeles esta contraseña: " + colPWD)

# preguntamos si la quiere almacenar usando gnu-pass

while True:
    WAREHOUSEd = input("¿Quieres almacenarla? (S)i o (N)o \n").strip().lower()
    if WAREHOUSEd not in ("s","n"):
        print(MEC2)
    else:
        break

if WAREHOUSEd == 's':
    WAREHOUSE = str(input("\n¿Cómo se llamará el almacén?\n"))
    COMMANDO = "pass add " + WAREHOUSE
    p = subprocess.Popen(COMMANDO, shell=True)
    p.communicate(input=PWD)

else:
    # por seguridad le damos un tiempo límite de guardado en el portapapeles
    print("\nEsta contraseña permanecerá en el portapapeles 30 segundos")

# seguimos preocupados por la seguridad ;)
print("\nEsta contraseña permanecerá en el portapapeles 30 segundos")

# creamos un contador por pantalla para ser conscientes del tiempo que le queda
# a la contraseña antes de ser borrada del portapapeles
ESPERA = 30

while ESPERA > 0:
    print("{:02d}".format(ESPERA), end='\r')
    time.sleep(1)
    ESPERA -= 1

# borramos el contenido del portapapeles
cb.copy('')
