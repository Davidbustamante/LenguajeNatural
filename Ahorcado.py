#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:02:07 2019

@author: davidbellobustamante
"""

p = ''
listaPalabraAdiv = []
listaPalabraMost = []
intentos = 5
letra = ''
run = True

print('\n')
print('_______A H O R C A D O_______\n')
p = input('Dime una palabra: ')

listaPalabraAdiv = list(p)
for item in listaPalabraAdiv:
    listaPalabraMost.append('_')

while run:
    print(' '.join(listaPalabraMost))

    letra = input('Escribe una letra: ')
    error = False

    if letra not in listaPalabraAdiv:
        error = True
        intentos = intentos - 1
        print('\n')
        print('¡FALLASTE! Te quedan {intentos} intentos'.format(intentos=intentos))
    else:
        for key, value in enumerate(listaPalabraAdiv):
            if value == letra:
                listaPalabraMost[key] = value

    if intentos <= 0:
        run = False
        print('¡PERDISTE!, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
    elif listaPalabraAdiv == listaPalabraMost:
        run = False
        print('\n')
        print('¡GANASTE!, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
