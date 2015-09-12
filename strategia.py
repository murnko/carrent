from numpy import random
from preprog import *

M = 21
policy = random.randint(-5, 5, (M, M))
Actions = [x for x in range(-5, 5)]

values = [[0 for x in range(M)] for x in range(M)]


def bellman(stani, stanj, akcja):
    hajsy = abs(akcja)*(-20)
    if akcja:
        stani += akcja
        stanj -= akcja
    else:
        stani -= akcja
        stanj += akcja

    if stani > 20:
        stani = 20
    elif stani < 0:
        stani = 0

    if stanj > 20:
        stani = 20
    elif stanj < 0:
        stani = 0




values_temp = values
for i in range(M): # to bedzie najbardziej zawila petla od czasu odwroconego wahadla
    for j in range(M):
        val_bell = []
        for a in Actions:
            val_bell = bellman(i,j,values[i][j])


        all_y
        values_temp[i][j] = all_y;




