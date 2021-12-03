# https://adventofcode.com/2021/day/3

def solution_part1(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

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


assert (solution_part1('input/day3.test.txt') == 198)
print('Result Part 1: ', solution_part1('input/day3.txt'))

# assert (solution_part2('input/day2.test.txt') == 900)
# print('Result Part 2: ', solution_part2('input/day2.txt'))
