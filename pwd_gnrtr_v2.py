#!/bin/env python

"""
Título:     Generador casero de contraseñas
Creador:    Nicolas Riquelme
Fecha:      2022-08-31

TODO en nuevas versiones:
    - añadir validación de longitud min y max
    - integrar con gnu-pass
"""

import string
import random
import pyfiglet
from termcolor import colored

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

# pintamos la contraseña
PWD = colored(PWD, 'yellow', attrs=[])

# y finalmente se la mostramos al usuario
print("\nHe generado esta contraseña para ti: " + PWD)
