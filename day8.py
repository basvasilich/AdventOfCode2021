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


def string_diff(a: str, b: str) -> str:
    a_set = set(a)
    b_set = set(b)
    if len(a_set) > len(b_set):
        r = "".join(b_set - a_set)
        return r
    else:
        r = "".join(a_set - b_set)
        return r


def solution_part1(filename: str, ) -> int:
    _, result_part1 = read_input(filename)
    return result_part1


def solution_part2(filename: str, ) -> int:
    vals, _ = read_input(filename)

    result = 0

    for inp_list, out_list in vals:
        digits = {}
        inp_list = ["".join(sorted(s)) for s in inp_list]
        for s in inp_list:
            if len(s) == 2:
                digits[1] = s
            elif len(s) == 3:
                digits[7] = s
            elif len(s) == 7:
                digits[8] = s
            elif len(s) == 4:
                digits[4] = s

        for s in inp_list:
            if len(s) == 6 and len(string_diff(s, digits[7])) == 1:
                digits[6] = s
            elif len(s) == 5 and len(string_diff(s, digits[1])) == 0:
                digits[3] = s

        c_char = string_diff(digits[6], digits[7])

        for s in inp_list:
            if len(s) == 6 and s not in digits.values() and len(string_diff(s, digits[4])) == 0:
                digits[9] = s
            elif len(s) == 5 and s not in digits.values() and c_char not in s:
                digits[5] = s

        for s in inp_list:
            if len(s) == 6 and s not in digits.values():
                digits[0] = s
            elif len(s) == 5 and s not in digits.values():
                digits[2] = s

        chars = {v: str(k) for k, v in digits.items()}
        result_list = [chars["".join(sorted(s))] for s in out_list]
        result_str = "".join(result_list)
        result += int(result_str)
    return result


assert (solution_part1('input/day8.test.txt') == 26)
print('Result Part 1: ', solution_part1('input/day8.txt'))

assert (solution_part2('input/day8.test.txt') == 61229)
print('Result Part 2: ', solution_part2('input/day8.txt'))
