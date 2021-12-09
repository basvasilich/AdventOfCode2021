# https://adventofcode.com/2021/day/6

def read_input(filename) -> (list[list[int]]):
    with open(filename) as file:
        return [[int(x) for x in list(line.rstrip("\n"))] for line in file.readlines()]


def solution_part1(filename: str, ) -> int:
    heightmap = read_input(filename)


    return 1


assert (solution_part1('input/day9.test.txt') == 15)
print('Result Part 1: ', solution_part1('input/day9.txt'))
