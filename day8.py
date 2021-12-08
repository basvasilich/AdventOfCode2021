# https://adventofcode.com/2021/day/6

def read_input(filename) -> (list[(list[str], list[str])], int):
    with open(filename) as file:
        lines = file.readlines()
        vals = []
        result_part1 = 0
        for line in lines:
            inp, out = line.rstrip("\n").split(" | ")
            inp_list = inp.split(" ")
            out_list = out.split(" ")
            for out_val in out_list:
                if len(out_val) in {2, 3, 4, 7}:
                    result_part1 += 1
            vals.append((inp_list, out_list))
        return vals, result_part1


def solution_part1(filename: str, ) -> int:
    _, result_part1 = read_input(filename)
    return result_part1


assert (solution_part1('input/day8.test.txt') == 26)
print('Result Part 1: ', solution_part1('input/day8.txt'))
#
# assert (solution('input/day7.test.txt', True) == 168)
# print('Result Part 2: ', solution('input/day7.txt', True))
