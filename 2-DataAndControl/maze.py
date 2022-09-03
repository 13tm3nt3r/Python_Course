# Create a map to move a @ through it
import readchar
import os
import random
import time

# X axis
POS_X = 0
# Y axis
POS_Y = 1
# Map dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 15
# List of lists where the different obstacles are going to be spawned
OBSTACLES_N = 10
map_objects = []
# New list to represent my tail
tail = []
tail_length = 0

my_position = [0, 0]


def random_obstacle():
    obs = 0
    while obs != OBSTACLES_N:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        # Check if there are repeated coordinates and if my_position != new_position
        if (new_position not in map_objects) and (new_position != my_position):
            map_objects.append(new_position)
            obs += 1

    return map_objects


def print_map(pos, map_objs, tail_length):
    # Output a line, the height of the map:
    print("+" + "-" * (MAP_WIDTH * 3) + "+")
    for y in range(MAP_HEIGHT):
        # Output: a line:
        print("|", end="")
        for x in range(MAP_WIDTH):
            # By default, a space:
            char_to_draw = " "
            # eated_pos = None

            i = 0
            # Counter to check each list of the map_objects, in case they match, put an obstacle
            for map_object in map_objs:
                if (x == map_object[POS_X]) and (y == map_object[POS_Y]):
                    # eated_pos = map_object
                    # When my_position == position of an obstacle, it disappears.
                    if (map_object[POS_X] == pos[POS_X]) and (map_object[POS_Y] == pos[POS_Y]):
                        # Convert to an empty sub_list
                        map_objs.pop(i)
                        # tail.append(0, i)
                        tail_length += 1
                    else:
                        char_to_draw = "*"
                i += 1

            for tail_item in tail:
                if (x == tail_item[POS_X]) and (y == tail_item[POS_Y]):
                    char_to_draw = "@"

            # Put a @ in the position given in my_position:
            if (x == pos[POS_X]) and (y == pos[POS_Y]):
                char_to_draw = "@"

                # if eated_pos:
                #     map_objs.remove(eated_pos)

            print(" {} ".format(char_to_draw), end="")

        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    print("The length of my tail is {}".format(tail_length))

    return tail_length


print("\nWELCOME TO THE GAME!")
# user_obstacles = int(input("GIVE ME THE NUMBER OF OBSTACLES THAT YOU WANT TO APPEAR IN THE MAP: "))
random_obstacle()
# Ask the user the next move:
while True:
    tail_length = print_map(my_position, map_objects, tail_length)
    direction = readchar.readchar()

    # Interactive movement
    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH

    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH

    elif direction == "q":
        print("\n\nBye!!\n")
        exit(0)

    os.system("cls")
