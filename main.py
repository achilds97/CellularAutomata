import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def check_neighbors(self, left, right, rule):
    rule_as_string = f'{rule:08b}'

    if left == 1 and self == 1 and right == 1:
        return int(rule_as_string[0])
    elif left == 1 and self == 1 and right == 0:
        return int(rule_as_string[1])
    elif left == 1 and self == 0 and right == 1:
        return int(rule_as_string[2])
    elif left == 1 and self == 0 and right == 0:
        return int(rule_as_string[3])
    elif left == 0 and self == 1 and right == 1:
        return int(rule_as_string[4])
    elif left == 0 and self == 1 and right == 0:
        return int(rule_as_string[5])
    elif left == 0 and self == 0 and right == 1:
        return int(rule_as_string[6])
    elif left == 0 and self == 0 and right == 0:
        return int(rule_as_string[7])


def get_next_step(arr, rule):
    new_step = []

    for i in range(len(arr)):

        if 0 < i < (len(arr) - 1):
            new_step.append(check_neighbors(arr[i], arr[i - 1], arr[i + 1], rule))
        elif i == 0:
            new_step.append(check_neighbors(arr[i], 0, arr[i + 1], rule))
        elif i == len(arr) - 1:
            new_step.append(check_neighbors(arr[i], arr[i - 1], 0, rule))

    return new_step


def init_classroom(size):
    arr = []

    for i in range(size):

        if i == int(size / 2):
            arr.append(1)
        else:
            arr.append(0)

    return arr


if __name__ == '__main__':

    height = 1000
    width = 100
    rule = 54
    classroom = [[]]
    classroom[0] = init_classroom(width)

    for x in range(height):
        classroom.append((get_next_step(classroom[x], rule)))

    cmap = colors.ListedColormap(['white', 'black'])
    bounds = [0, 0.5, 1]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(classroom, cmap=cmap, norm=norm)

    plt.show()
