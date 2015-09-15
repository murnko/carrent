from numpy import random
import copy
from preprog import *


M = 21
new_policy = [[0 for x in range(M)] for x in range(M)]

Actions = [x for x in range(-5, 5)]

values = [[0 for x in range(M)] for x in range(M)]
policy = [[1 for x in range(M)] for x in range(M)]
reward = [[0 for x in range(M)] for x in range(M)]


for x in range(M):  # to bedzie najbardziej zawila petla od czasu odwroconego wahadla
        for y in range(M):
            hajsy = 0
            hajsy2 = 0
            for i in range(len(park1rent)):
                for j in range(len(park2rent)):
                    hajsy += min(i, x)*100*park1rent[i] + min(j, y)*100*park2rent[j]
                    print(hajsy)
                hajsy2 += hajsy
                print(hajsy2)
            reward[x][y] = hajsy2/441
printer_f(reward)
z = 0
iterate = 1
while iterate == 1:
    z += 1
    policy = copy.deepcopy(new_policy)
    for x in range(M):
        for y in range(M):
            hajsy = []
            for a in Actions:
                hajs = 0
                for (cars1, prob1) in change1.items():
                    for (cars2, prob2) in change2.items():
                        if a > y+cars2 or -a > x+cars1:
                            continue
                        stan1 = 20 if (x+a+cars1) >= 20 else 0 if (x+a+cars1) <= 0 else x+a+cars1
                        stan2 = 20 if (y-a+cars2) >= 20 else 0 if (y-a+cars2) <= 0 else y-a+cars2
                        prob = prob1 * prob2
                        hajs += prob * (reward[x][y] - (abs(a)*20) + values[stan1][stan2])
                hajsy.append(0.9*hajs)
            #print(hajsy)
            s = max(hajsy)
            for i, j in enumerate(hajsy):
                if j == s:
                    new_policy[x][y] = Actions[i]

    print("\n"+"Iteracja" + str(z))
    iterate = diff = 0
    for x in range(M):
        for y in range(M):
            if not (policy[x][y] == new_policy[x][y]):
                iterate = 1
                diff += 1
    printer(new_policy)
    print(diff)

    if iterate == 0:
        break

    for x in range(M):
        for y in range(M):
            a = new_policy[x][y]
            hajs = 0
            for (cars1, prob1) in change1.items():
                for (cars2, prob2) in change2.items():
                    if a > y+cars2 or -a > x+cars1:
                        continue
                    stan1 = 20 if (x+a+cars1) >= 20 else 0 if (x+a+cars1) <= 0 else x+a+cars1
                    stan2 = 20 if (y-a+cars2) >= 20 else 0 if (y-a+cars2) <= 0 else y-a+cars2
                    prob = prob1 * prob2
                    hajs += prob * (reward[x][y] - (abs(a)*20) + values[stan1][stan2])
            values[x][y] = 0.9*hajs


