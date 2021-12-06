# https://adventofcode.com/2021/day/6

def read_input(filename) -> list[(str, int)]:
    with open(filename) as file:
        line = file.readlines()
        return [int(x) for x in line[0].rstrip("\n").split(',')]


def solution(filename, day) -> int:
    store = [0] * 9
    input_vals = read_input(filename)

    for val in input_vals:
        store[val] += 1

    while day:
        tmp = [0] * 9
        val_0 = store[0]

        for i in range(1, 9):
            tmp[i - 1] = store[i]
        tmp[8] += val_0
        tmp[6] += val_0
        store = tmp
        day -= 1

    return sum(store)


assert (solution('input/day6.test.txt', 80) == 5934)
print('Result Part 1: ', solution('input/day6.txt', 80))

assert (solution('input/day6.test.txt', 256) == 26984457539)
print('Result Part 1: ', solution('input/day6.txt', 256))
