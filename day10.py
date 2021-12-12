# https://adventofcode.com/2021/day/10

from heapq import heappop, heappush

char_map = {"}": ("{", 1197, 3), ">": ("<", 25137, 4), ")": ("(", 3, 1), "]": ("[", 57, 2)}
inv_char_map = {char_map[c][0]: char_map[c][2] for c in char_map.keys()}


def read_input(filename) -> list[str]:
    with open(filename) as file:
        return [line.rstrip("\n") for line in file.readlines()]


def solution_part1(filename: str, ) -> (int, list[list[str]]):
    lines = read_input(filename)
    result = 0
    incomplete = []

    for line in lines:
        s = []
        last = None
        for index, char in enumerate(line):
            if len(s):
                last = s[-1]

            if last and char in char_map.keys() and char_map[char][0] == last:
                s.pop()
                if index == len(line) - 1 and len(s):
                    incomplete.append(s)
            elif (not len(s) and char in char_map.keys()) or char in char_map.keys():
                result += char_map[char][1]
                break
            elif index == len(line) - 1 and len(s):
                s.append(char)
                incomplete.append(s)
            else:
                s.append(char)

    return result, incomplete


def solution_part2(filename: str, ) -> int:
    _, incomplete = solution_part1(filename)
    heap = []

    for arr in incomplete:
        result = 0
        for i in range(len(arr) - 1, -1, -1):
            char = arr[i]
            result *= 5
            result  += inv_char_map[char]

        heappush(heap, result)

    mid = len(heap) // 2

    while mid:
        heappop(heap)
        mid -= 1

    return heappop(heap)


assert (solution_part1('input/day10.test.txt')[0] == 26397)
print('Result Part 1: ', solution_part1('input/day10.txt')[0])

assert (solution_part2('input/day10.test.txt') == 288957)
print('Result Part 1: ', solution_part2('input/day10.txt'))
