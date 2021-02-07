'''
!/usr/local/bin/python3 - Não funcionou
'''
from math import pi

if __name__ == '__main__':
    raio = input('Informe o raio: ')  # float em raio, entrada str
    print('Área do círculo', pi * float(raio) ** 2)

print('Nome do módulo', __name__)
