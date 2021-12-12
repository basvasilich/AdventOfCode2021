# https://adventofcode.com/2021/day/11
from common import get_neighbors


def read_input(filename) -> list[list[int]]:
    with open(filename) as file:
        return [[int(x) for x in list(line.rstrip("\n"))] for line in file.readlines()]


def day_helper(matrix) -> (list[list[int]], int):
    flashes = []
    step_count = 0

    def process_flash(row, col):
        neighbors = get_neighbors(matrix, row, col)
        for item in neighbors:
            i, j = item[1]
            if matrix[i][j] == 0:
                pass
            elif matrix[i][j] == 9:
                flashes.append((i, j))
                matrix[i][j] = 0
            else:
                matrix[i][j] += 1

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 9:
                matrix[row][col] = 0
                flashes.append((row, col))
            else:
                matrix[row][col] += 1
    while len(flashes):
        row, col = flashes.pop()
        step_count += 1
        process_flash(row, col)

    return matrix, step_count


def solution_part1(filename: str, steps: int) -> int:
    matrix = read_input(filename)
    flashes_count = 0

    while steps:
        matrix, step_count = day_helper(matrix)
        flashes_count += step_count
        steps -= 1

    return flashes_count


def solution_part2(filename: str) -> int:
    matrix = read_input(filename)
    steps = 0
    step_count = 0

    while step_count != 100:
        matrix, step_count = day_helper(matrix)
        steps += 1

    return steps


assert (solution_part1('input/day11.test.txt', 10) == 204)
assert (solution_part1('input/day11.test.txt', 100) == 1656)
print('Result Part 1: ', solution_part1('input/day11.txt', 100))

assert (solution_part2('input/day11.test.txt') == 195)
print('Result Part 2: ', solution_part2('input/day11.txt'))
