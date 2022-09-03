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
my_position = [0, 0]


def random_obstacle():
    for obs in range(OBSTACLES_N):
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        # Check if there are repeated coordinates and if my_position != new_position
        if (new_position not in map_objects) and (new_position != my_position):
            map_objects.append(new_position)

    return map_objects


def print_map(pos, map_objs):
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
                    else:
                        char_to_draw = "*"
                i += 1

            # Put a @ in the position given in my_position:
            if (x == pos[POS_X]) and (y == pos[POS_Y]):
                char_to_draw = "@"

                # if eated_pos:
                #     map_objs.remove(eated_pos)

            print(" {} ".format(char_to_draw), end="")

        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")


# Interactive movement (WASD):
# direction = input("Where do you want to move next? (WASD): ")
def interactive_mov(pos):
    direction = readchar.readchar()

    if direction == "w":
        pos[POS_Y] -= 1
        # When user goes from down to up and viceversa (Y axis)
        # if pos[POS_Y] < 0:
        #     pos[POS_Y] = (MAP_HEIGHT - 1)
        pos[POS_Y] %= MAP_HEIGHT

    elif direction == "s":
        pos[POS_Y] += 1
        # if pos[POS_Y] > (MAP_HEIGHT - 1):
        #     pos[POS_Y] = 0
        pos[POS_Y] %= MAP_HEIGHT

    elif direction == "a":
        pos[POS_X] -= 1
        # When user goes from left to right and viceversa (X axis)
        # if pos[POS_X] < 0:
        #     pos[POS_X] = MAP_WIDTH - 1
        pos[POS_X] %= MAP_WIDTH

    elif direction == "d":
        pos[POS_X] += 1
        # if pos[POS_X] > (MAP_WIDTH - 1):
        #     pos[POS_X] = 0
        pos[POS_X] %= MAP_WIDTH

    elif direction == "q":
        print("\n\nBye!!\n")
        exit(0)

    return pos


print("\nWELCOME TO THE GAME!")
# user_obstacles = int(input("GIVE ME THE NUMBER OF OBSTACLES THAT YOU WANT TO APPEAR IN THE MAP: "))
random_obstacle()
# Ask the user the next move:
while True:
    print_map(my_position, map_objects)
    my_position = interactive_mov(my_position)
    os.system("cls")
