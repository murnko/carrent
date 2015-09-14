
from math import *

def pss(n, lam):
    return ((lam**n)/factorial(n))*exp(-lam)

#  prawdopodobienstwa wg poissona
park1rent = []  # 3
park2rent = []  # 4
park1back = []  # 3
park2back = []  # 2

for x in range(9):
    pr = pss(x, 2)
    park2back.append(pr)
    pr = pss(x, 3)
    park1back.append(pr)
    park1rent.append(pr)
    pr = pss(x, 4)
    park2rent.append(pr)



def printer(matrix):
    for i in range(21):
        for j in range(21):
            print("{:2d} ".format(matrix[i][j]), end='')
        print()

def printer_f(matrix):
    for i in range(21):
        for j in range(21):
            print("{:2f} ".format(matrix[i][j]), end='')
        print()

        # wstepne obliczenie to iteracja prawdopodobienstw zwrotow j na prawd. "wziasciow" i
        # przy sprawdzaniu warunku i <= x+j+a; przy czym a zmienia znak dla parkingu drugiego