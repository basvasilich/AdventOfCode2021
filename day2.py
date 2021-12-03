# https://adventofcode.com/2021/day/2
from enum import Enum


class Directions(Enum):
    up = 'up'
    down = 'down'
    forward = 'forward'


def solution_part1(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [(line.rstrip().split(' ')[0], int(line.rstrip().split(' ')[1])) for line in lines]

    if len(lines) == 0:
        return 0

    x_l = 0
    y_l = 0

    for i in range(0, len(lines)):
        direction, value = lines[i]

        if direction == Directions.forward.value:
            x_l += value
        elif direction == Directions.up.value:
            y_l -= value
        elif direction == Directions.down.value:
            y_l += value

    return abs(x_l * y_l)


def solution_part2(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [(line.rstrip().split(' ')[0], int(line.rstrip().split(' ')[1])) for line in lines]

    if len(lines) == 0:
        return 0

    x_l = 0
    y_l = 0
    aim = 0

    for i in range(0, len(lines)):
        direction, x = lines[i]

        if direction == Directions.forward.value:
            x_l += x
            y_l += x * aim
        elif direction == Directions.up.value:
            aim -= x
        elif direction == Directions.down.value:
            aim += x

    return abs(x_l * y_l)


assert (solution_part1('input/day2.test.txt') == 150)
print('Result Part 1: ', solution_part1('input/day2.txt'))

assert (solution_part2('input/day2.test.txt') == 900)
print('Result Part 2: ', solution_part2('input/day2.txt'))
