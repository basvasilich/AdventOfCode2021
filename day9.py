# https://adventofcode.com/2021/day/9
from collections import deque
from common import get_neighbors


def read_input(filename) -> (list[list[int]]):
    with open(filename) as file:
        return [[int(x) for x in list(line.rstrip("\n"))] for line in file.readlines()]


def solution_part1(filename: str, ) -> (int, set[(int, int)]):
    heightmap = read_input(filename)
    row_l = len(heightmap)

    low_points = set()
    result = 0

    for row in range(row_l):
        col_l = len(heightmap[row])
        for col in range(col_l):
            item = heightmap[row][col]
            neighbors = get_neighbors(heightmap, row, col)
            if min(item, *[x[0] for x in neighbors]) == item:
                result += 1 + item
                low_points.add((row, col))
    return result, low_points


def solution_part2(filename: str, ) -> int:
    _, low_points = solution_part1(filename)
    heightmap = read_input(filename)
    result = []
    q = deque()
    for row, col in low_points:
        visited = {(row, col)}
        count = 1
        item = heightmap[row][col]
        q.extend(filter(lambda x: x[0] - item == 1 and x[1] not in visited, get_neighbors(heightmap, row, col)))
        while len(q):
            check_item = q.popleft()
            if check_item[1] not in visited:
                count += 1
                q.extend(filter(lambda x: x[0] < 9 and x[0] - check_item[0] == 1 and x[1] not in visited,
                                get_neighbors(heightmap, check_item[1][0], check_item[1][1])))
            visited.add(check_item[1])

        result.append(count)
    result.sort(reverse=True)

    prod = 1
    for v in range(3):
        prod *= result[v]

    return prod


assert (solution_part1('input/day9.test.txt')[0] == 15)
print('Result Part 1: ', solution_part1('input/day9.txt')[0])
assert (solution_part2('input/day9.test.txt') == 1134)
print('Result Part 2: ', solution_part2('input/day9.txt'))
