# https://adventofcode.com/2021/day/7

def read_input(filename) -> list[(str, int)]:
    with open(filename) as file:
        line = file.readlines()
        return [int(x) for x in line[0].rstrip("\n").split(',')]


def solution(filename: str, part2: bool = False) -> int:
    vals = read_input(filename)

    memo = {}

    def calculate_fuel(vals, point, part2):
        if point in memo:
            return memo[point]

        result = 0
        if part2:
            for val in vals:
                n = abs(point - val)
                result += (pow(n, 2) + n) / 2
        else:
            for val in vals:
                result += abs(point - val)

        memo[point] = result
        return result

    def helper(s, e, _min_fuel, part2):
        if e < s:
            return _min_fuel

        if e == s:
            return min(_min_fuel, calculate_fuel(vals, s, part2))

        mid = s + (e - s) // 2

        s_fuel = calculate_fuel(vals, s, part2)
        e_fuel = calculate_fuel(vals, e, part2)
        mid_fuel = calculate_fuel(vals, mid, part2)
        _min_fuel = min(s_fuel, e_fuel, mid_fuel, _min_fuel)

        if abs(s_fuel - mid_fuel) > abs(e_fuel - mid_fuel):
            return helper(mid + 1, e, _min_fuel, part2)
        else:
            return helper(s, mid, _min_fuel, part2)

    max_val = max(vals)

    min_fuel = max_val * len(vals)

    if part2:
        min_fuel = (max_val * (max_val + 1) * len(vals)) / 2

    return helper(min(vals), max_val, min_fuel, part2)


assert (solution('input/day7.test.txt') == 37)
print('Result Part 1: ', solution('input/day7.txt'))

assert (solution('input/day7.test.txt', True) == 168)
print('Result Part 2: ', solution('input/day7.txt', True))
