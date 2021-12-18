# https://adventofcode.com/2021/day/13


def read_input(filename) -> ():
    points = {"x": {}, "y": {}, "all": set()}
    folds = []

    with open(filename) as file:
        for line in file.readlines():
            if 'fold' in line:
                if "x" in line:
                    _, x = line.rstrip("\n").split("=")
                    folds.append(('x', int(x)))
                else:
                    _, y = line.rstrip("\n").split("=")
                    folds.append(('y', int(y)))
            elif ',' in line:
                x, y = [int(i) for i in line.rstrip("\n").split(",")]
                points['all'].add((x, y))
                if x not in points['x'].keys():
                    points['x'][x] = set()
                if y not in points['y'].keys():
                    points['y'][y] = set()

                points['x'][x].add(y)
                points['y'][y].add(x)

    return points, folds


def make_fold(fold_points, fold):
    axis, fold_val = fold

    filtered_axis_vals = list(filter(lambda i: i >= fold_val, fold_points[axis].keys()))

    for axis_val in filtered_axis_vals:
        if axis == 'x':
            y_vals = fold_points[axis][axis_val]
            for y in y_vals:
                fold_points["all"].discard((axis_val, y))
                new_x = 2 * fold_val - axis_val
                fold_points["all"].add((new_x, y))
                if new_x not in fold_points['x'].keys():
                    fold_points['x'][new_x] = set()

                fold_points["x"][new_x].add(y)
        else:
            x_vals = fold_points[axis][axis_val]
            for x in x_vals:
                fold_points["all"].discard((x, axis_val))
                new_y = 2 * fold_val - axis_val
                fold_points["all"].add((x, new_y))
                if new_y not in fold_points['y'].keys():
                    fold_points['y'][new_y] = set()

                fold_points["y"][new_y].add(x)
        del fold_points[axis][axis_val]
    return fold_points


def print_points(points):
    s = ''
    for row in range(max(points['y'].keys()) + 1):
        for col in range(max(points['x'].keys()) + 1):
            if (col, row) in points["all"]:
                s += "#"
            else:
                s += "."
        s += '\n'

    print(s)


def solution_part1(filename: str) -> int:
    points, folds = read_input(filename)

    points = make_fold(points, folds[0])

    return len(points['all'])


def solution_part2(filename: str):
    points, folds = read_input(filename)
    print_points(points)

    for fold in folds:
        print_points(points)
        points = make_fold(points, fold)

    print_points(points)


assert (solution_part1('input/day13.test.txt') == 17)
# print('Result Part 1: ', solution_part1('input/day13.txt'))

solution_part2('input/day13.test.txt')
# solution_part2('input/day13.txt')
