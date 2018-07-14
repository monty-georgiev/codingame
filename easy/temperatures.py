#!/usr/bin/python3

n = int(input())

tempMax = 5526
tempMin = -273
closest = 0


for i in input().split():

    t = int(i)  # t :temperature expressed as an integer between -273 an 5526

    if t < tempMax and t > 0:
        tempMax = t
        closest = t
    elif t > tempMin and t < 0:
        tempMin = t

        if abs(t) < tempMax:
            closest = t

print(closest)
