from numpy import random
from preprog import *

M = 21
new_policy = [[0 for x in range(M)] for x in range(M)]

Actions = [x for x in range(-5, 5)]

values = [[0 for x in range(M)] for x in range(M)]
policy = [[1 for x in range(M)] for x in range(M)]


for z in range(M):
    policy = new_policy
    for x in range(M):  # to bedzie najbardziej zawila petla od czasu odwroconego wahadla
        for y in range(M):
            hajsy = 0
            a = policy[x][y]
            for i in range(len(park1rent)):
                for j in range(len(park1back)):
                    if i <= x+a:
                        hajsy += i * 100 * park1rent[i]
                    else:
                        if i <= x+a+j:
                            hajsy += (x+a) * 100 * park1rent[i]
                            hajsy += (i - x - a)*100*park1rent[i]*park1back[j]
                        else:
                            hajsy += (x+a+j) * 100 * park1rent[i]

            for i in range(len(park2rent)):
                for j in range(len(park2back)):
                    if i <= y-a:
                        hajsy += i * 100 * park2rent[i]
                    else:
                        if i <= y-a+j:
                            hajsy += (y-a) * 100 * park2rent[i]
                            hajsy += (i - y + a)*100*park2rent[i]*park2back[j]
                        else:
                            hajsy += (y-a+j) * 100 * park1rent[i]

            values[x][y] = hajsy
    #printer_f(values)

    for x in range(M):
        for y in range(M):
            hajsy = []
            for a in Actions:
                hajs = 0
                for i in range(len(park1back)):
                    for j in range(len(park2back)):
                        stan1 = 20 if (x+a+i) >= 20 else 0 if (x+a+i) <= 0 else x+a+i
                        stan2 = 20 if (y-a+j) >= 20 else 0 if (y-a+j) <= 0 else y-a+j
                        hajs += values[stan1][stan2]*park1back[i]*park2back[j]
                hajsy.append(hajs)
            #print(hajsy)
            s = max(hajsy)
            for i, j in enumerate(hajsy):
                if j == s:
                    new_policy[x][y] = Actions[i]
    print("\n"+"Iteracja" + str(z))
    printer(new_policy)

