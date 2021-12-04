# https://adventofcode.com/2021/day/4


def read_input(filename) -> (
        list[int],
        list[{'rows': list[set[int]], 'cols': list[set[int]], 'items': set[int], 'ended': bool}]):
    nums = []
    boards = []
    with open(filename) as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if index == 0:
                nums = [int(num) for num in line.rstrip().split(',')]
            elif line == '\n':
                boards.append({'rows': [], 'cols': [set(), set(), set(), set(), set()], 'items': set(),
                               'ended': False})

            else:
                cur_board = boards[-1]
                row = ' '.join(line.split()).rstrip("\n").split(' ')
                row = [int(num) for num in row]
                cur_board['items'].update(row)
                cur_board['rows'].append(set(row))
                for i, item in enumerate(row):
                    cur_board['cols'][i].add(item)

        return nums, boards


def solution_part1(filename) -> int:
    nums, boards = read_input(filename)

    if len(boards) == 0 or len(nums) == 0:
        return 0

    for num in nums:
        for board in boards:
            if num in board['items']:
                for row in board['rows']:
                    if num in row:
                        row.remove(num)
                        board['items'].discard(num)
                        if len(row) == 0:
                            return num * sum(board['items'])
                for col in board['cols']:
                    if num in col:
                        col.remove(num)
                        board['items'].discard(num)
                        if len(col) == 0:
                            return num * sum(board['items'])
    return 0


def solution_part2(filename) -> int:
    nums, boards = read_input(filename)

    if len(boards) == 0 or len(nums) == 0:
        return 0

    win_count = 0

    for num in nums:
        for board in boards:
            win_flag = False
            if num in board['items'] and not board['ended']:
                for row in board['rows']:
                    if num in row and len(row):
                        row.discard(num)
                        board['items'].discard(num)
                        if len(row) == 0:
                            board['ended'] = True
                            win_count += 1
                            win_flag = True
                            if len(boards) == win_count:
                                total_sum = sum(board['items'])
                                return num * total_sum
                if not win_flag:
                    for col in board['cols']:
                        if num in col and len(col):
                            col.discard(num)
                            board['items'].discard(num)
                            if len(col) == 0:
                                board['ended'] = True
                                win_count += 1
                                if len(boards) == win_count:
                                    total_sum = sum(board['items'])
                                    return num * total_sum
    return 0


assert (solution_part1('input/day4.test.txt') == 4512)
print('Result Part 1: ', solution_part1('input/day4.txt'))

assert (solution_part2('input/day4.test.txt') == 1924)
print('Result Part 2: ', solution_part2('input/day4.txt'))
