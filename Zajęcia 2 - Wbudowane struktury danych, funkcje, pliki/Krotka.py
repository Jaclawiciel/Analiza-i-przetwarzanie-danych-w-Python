import math


def pole_kola(promien):
    return math.pi * pow(promien, 2)


def obwod_kola(promien):
    return 2 * math.pi * promien


def pole_i_obwod_kola(promien):
    return pole_kola(promien), obwod_kola(promien)


print(pole_i_obwod_kola(4))
