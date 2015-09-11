#!/usr/bin/env python
# -*- coding: utf-8 -*-
# prawdopodobienstwo wypozyczenie
# prawdopodobienstwo oddania
# wspolczynnik dyskontowy V = 0.9
# za wypozyczony samochod 100pln
# transport pojedynczego samochodu 20pln i maksymalnie 5
from numpy import random
from math import *
# This is just a dummy solution that shows the required output format

M = 20
policy = random.randint(-5, 5, (M+1, M+1))

for i in range(M+1):
    for j in range(M+1):
        print("{:2d} ".format(policy[i][j]), end='')
    print()


def pss(n, lam):
    return ((lam**n)/factorial(n))*exp(1)**-lam

States = [[0 for x in range(21)] for x in range(21)]
actions = [x for x in range(-5, 6)]
