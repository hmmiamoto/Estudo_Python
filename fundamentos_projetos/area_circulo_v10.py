#!/usr/bin/python3

from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # Junto com o comando de execução devemos passar parameto
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
