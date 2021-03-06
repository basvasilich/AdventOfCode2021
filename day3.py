# https://adventofcode.com/2021/day/3


def read_input(filename) -> list[str]:
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def solution_part1(filename):
    lines = read_input(filename)

    if len(lines) == 0:
        return 0

    gamma_rate = ''
    epsilon_rate = ''

    gamma_rate_bites_counters = [(0, 0)] * len(lines[0])

    for line_index in range(0, len(lines)):
        bites = list(lines[line_index])

        for bite_index, bite in enumerate(bites):
            c_0, c_1 = gamma_rate_bites_counters[bite_index]
            if int(bite):
                gamma_rate_bites_counters[bite_index] = (c_0, c_1 + 1)
            else:
                gamma_rate_bites_counters[bite_index] = (c_0 + 1, c_1)

    for counter_0, counter_1 in gamma_rate_bites_counters:
        if counter_0 >= counter_1:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def solution_part2(filename):
    lines = read_input(filename)

    if len(lines) == 0:
        return 0

    def helper(lines_list: list[str], index: int, oxy: bool) -> str:
        if len(lines_list) == 1:
            return lines_list[0]

        list_0 = []
        list_1 = []
        for line in lines_list:
            line_bites = list(line)
            bite = int(line_bites[index])
            if bite:
                list_1.append(line)
            else:
                list_0.append(line)

        if len(list_1) > len(list_0):
            if oxy:
                return helper(list_1, index + 1, oxy)
            else:
                return helper(list_0, index + 1, oxy)
        elif len(list_1) == len(list_0):
            if oxy:
                return helper(list_1, index + 1, oxy)
            else:
                return helper(list_0, index + 1, oxy)
        else:
            if oxy:
                return helper(list_0, index + 1, oxy)
            else:
                return helper(list_1, index + 1, oxy)

    return int(helper(lines, 0, True), 2) * int(helper(lines, 0, False), 2)


assert (solution_part1('input/day3.test.txt') == 198)
print('Result Part 1: ', solution_part1('input/day3.txt'))

assert (solution_part2('input/day3.test.txt') == 230)
print('Result Part 2: ', solution_part2('input/day3.txt'))
