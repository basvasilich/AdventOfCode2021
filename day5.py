# https://adventofcode.com/2021/day/5


def solution_part1(filename) -> (int, set[int], set[int]):
    store = set()
    result = set()
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            vent1, vent2 = line.rstrip('\n').split(' -> ')
            x1, y1 = [int(i) for i in vent1.split(',')]
            x2, y2 = [int(i) for i in vent2.split(',')]
            if x1 == x2 and y1 != y2:
                y_g = max(y1, y2)
                y_l = min(y1, y2)
                while y_g >= y_l:
                    new_point = (x1, y_g)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    y_g -= 1
            elif y1 == y2 and x1 != x2:
                x_g = max(x1, x2)
                x_l = min(x1, x2)
                while x_g >= x_l:
                    new_point = (x_g, y1)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    x_g -= 1

    return len(result)


def solution_part2(filename) -> int:
    store = set()
    result = set()
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            vent1, vent2 = line.rstrip('\n').split(' -> ')
            x1, y1 = [int(i) for i in vent1.split(',')]
            x2, y2 = [int(i) for i in vent2.split(',')]
            if x1 == x2 and y1 != y2:
                y_g = max(y1, y2)
                y_l = min(y1, y2)
                while y_g >= y_l:
                    new_point = (x1, y_g)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    y_g -= 1
            elif y1 == y2 and x1 != x2:
                x_g = max(x1, x2)
                x_l = min(x1, x2)
                while x_g >= x_l:
                    new_point = (x_g, y1)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    x_g -= 1
            elif x2 == x1 and y1 == y2:
                new_point = (x1, y1)
                if new_point in store and new_point not in result:
                    result.add(new_point)
                store.add(new_point)
            elif x1 < x2 and y1 < y2:
                while x1 <= x2 and y1 <= y2:
                    new_point = (x1, y1)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    x1 += 1
                    y1 += 1
            elif x1 < x2 and y1 > y2:
                while x1 <= x2 and y1 >= y2:
                    new_point = (x1, y1)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    x1 += 1
                    y1 -= 1
            elif x1 > x2 and y1 < y2:
                while x1 >= x2 and y1 <= y1:
                    new_point = (x1, y1)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    x1 -= 1
                    y1 += 1
            elif x1 > x2 and y1 > y2:
                while x1 >= x2 and y1 >= y2:
                    new_point = (x1, y1)
                    if new_point in store and new_point not in result:
                        result.add(new_point)
                    store.add(new_point)
                    x1 -= 1
                    y1 -= 1

    return len(result)


assert (solution_part1('input/day5.test.txt') == 5)
print('Result Part 1: ', solution_part1('input/day5.txt'))

assert (solution_part2('input/day5.test.txt') == 12)
print('Result Part 2: ', solution_part2('input/day5.txt'))
