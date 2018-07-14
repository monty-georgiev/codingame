#! /usr/bin/python3
import math

n = int(input())
cities = []
'''
for i in range(n):
    x, y = [int(j) for j in input().split()]
    cities.append((x, y))
'''

cities = [(9, 12), (24, 15), (12, 30), (4, 3), (13, 27)]


def calculate_shortest_distance(cities, index):
    closest_index = 0
    closest_distance = 1000

    start_x, start_y = cities[index]
    del cities[index]

    for i in range(len(cities)):
        cityX, cityY = cities[i]
        deltaX = math.fabs(cityX - start_x)
        deltaY = math.fabs(cityY - start_y)
        distance = math.floor(math.sqrt(deltaX ** 2 + deltaY ** 2))

        if distance < closest_distance:
            closest_distance = distance
            closest_index = i

    if len(cities) == 1:
        return 0
    else:
        return closest_distance + calculate_shortest_distance(cities, closest_index)


total = calculate_shortest_distance(cities, 0)
print(total)
