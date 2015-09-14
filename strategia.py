from numpy import random
import copy
from preprog import *


M = 21
new_policy = [[0 for x in range(M)] for x in range(M)]

Actions = [x for x in range(-5, 5)]

values = [[0 for x in range(M)] for x in range(M)]
policy = [[1 for x in range(M)] for x in range(M)]
reward = [[0 for x in range(M)] for x in range(M)]
changes = 1

for x in range(M):  # to bedzie najbardziej zawila petla od czasu odwroconego wahadla
        for y in range(M):
            hajsy = 0
            for i in range(len(park1rent)):
                    if i <= x:
                        hajsy += i * 100
                    else:
                        hajsy += x * 100

            for i in range(len(park2rent)):
                    if i <= y:
                        hajsy += i * 100
                    else:
                        hajsy += y * 100
            reward[x][y] = hajsy
z = 0
while changes == 1:

    z += 1
    policy = copy.deepcopy(new_policy)

    for x in range(M):
        for y in range(M):
            hajsy = []
            for a in Actions:
                hajs = 0
                for i in range(len(park1back)):
                    for k in range(len(park2back)):
                        for j in range(len(park1rent)):
                            for l in range(len(park2rent)):
                                if a > y+k-l or -a > x+i-j:
                                    continue
                                stan1 = 20 if (x+a+i-j) >= 20 else 0 if (x+a+i-j) <= 0 else x+a+i-j
                                stan2 = 20 if (y-a+k-l) >= 20 else 0 if (y-a+k-l) <= 0 else y-a+k-l
                                prob = park1back[i]*park2back[k]*park1rent[j]*park2rent[l]
                                hajs += prob * (reward[x][y] - (abs(a)*20) + values[stan1][stan2])
                hajsy.append(0.9*hajs)

            #print(hajsy)
            s = max(hajsy)
            for i, j in enumerate(hajsy):
                if j == s:
                    new_policy[x][y] = Actions[i]

    print("\n"+"Iteracja" + str(z))
    changes = 0
    for x in range(M):
        for y in range(M):
            if not (policy[x][y] == new_policy[x][y]):
                changes = 1
    printer(new_policy)

    if changes == 0:
        break

    for x in range(M):
        for y in range(M):
            a = new_policy[x][y]
            hajs = 0
            for i in range(len(park1back)):
                for k in range(len(park2back)):
                    for j in range(len(park1rent)):
                        for l in range(len(park2rent)):
                            if a > y+k-l or -a > x+i-j:
                                continue
                            stan1 = 20 if (x+a+i-j) >= 20 else 0 if (x+a+i-j) <= 0 else x+a+i-j
                            stan2 = 20 if (y-a+k-l) >= 20 else 0 if (y-a+k-l) <= 0 else y-a+k-l
                            prob = park1back[i]*park2back[k]*park1rent[j]*park2rent[l]
                            hajs += 0.9 * prob * (reward[x][y] - (abs(a)*20) + values[stan1][stan2])
            values[x][y] = hajs


