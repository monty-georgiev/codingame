#! /usr/bin/python3


light_x, light_y, current_x, current_y = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())


    #EAST
    if light_y > current_x:
        if light_y > current_y:
            print("SE")
        elif light_y == current_y:
            print("E")

        current_x += 1

    #WEST
    if light_x < current_x:
        if light_y > current_y:
            print("SW")
        elif light_y == current_y:
            print("W")
        else:
            print("NW")
        
        current_x -= 1

    #NORTH
    if light_y < current_y:
        if light_x > current_x:
            print("NE")
        elif light_x == current_x:
            print("N")

        current_y -= 1

    #SOUTH
    if light_y > current_y:
        if light_x == current_x:
            print("S")

        current_y += 1
