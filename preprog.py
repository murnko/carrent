
from math import *

def pss(n, lam):
    return ((lam**n)/factorial(n))*exp(-lam)

#  prawdopodobienstwa wg poissona
park1rent = []  # 3
park2rent = []  # 4
park1back = []  # 3
park2back = []  # 2

for x in range(21):
    pr = pss(x, 2)
    park2back.append(pr)
    pr = pss(x, 3)
    park1back.append(pr)
    park1rent.append(pr)
    pr = pss(x, 4)
    park2rent.append(pr)

change1 = {}
for i in range(len(park1back)):
    for j in range(len(park1rent)):
        change1[i - j] = change1.get(i-j, 0) + park1back[i]*park1rent[j]

change2 = {}
for i in range(len(park2back)):
    for j in range(len(park2rent)):
        change2[i - j] = change2.get(i-j, 0) + park2back[i]*park2rent[j]

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

