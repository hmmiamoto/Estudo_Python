'''
!/usr/local/bin/python3 - Não funcionou
'''
from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')  # float em raio, entrada str
    area = circulo(raio)
    print('Área do círculo', area)
