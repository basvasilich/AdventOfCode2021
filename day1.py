# https://adventofcode.com/2021/day/1

def solution_part1(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    if len(lines) == 0:
        return 0

    count_increase = 0
    prev_line = lines[0]

    for i in range(1, len(lines)):
        line = lines[i]

        if prev_line < line:
            count_increase += 1

        prev_line = line

    return count_increase

def solution_part2(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    if len(lines) == 0:
        return 0

    count_increase = 0
    prev_sum = lines[0] + lines[1] + lines[2]

    for i in range(0, len(lines) - 3):
        sum = prev_sum - lines[i] + lines[i + 3]

        if prev_sum  < sum:
            count_increase += 1

        prev_sum = sum

    return count_increase


assert(solution_part1('input/day1.test.txt') == 7)
print('Result Part 1: ', solution_part1('input/day1.txt'))
assert(solution_part2('input/day1.test.txt') == 5)
print('Result Part 2: ', solution_part2('input/day1.txt'))
