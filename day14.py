# https://adventofcode.com/2021/day/14


class Node:
    def __init__(self, val: str = ''):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None


def read_input(filename) -> ():
    initial_list = LinkedList()
    char_map = {}

    with open(filename) as file:
        for index, line in enumerate(file.readlines()):
            if index == 0:
                list_chars = list(line.rstrip("\n"))
                prev_node = Node(list_chars[0])
                initial_list.head = prev_node
                for char_index in range(1, len(list_chars)):
                    tmp_node = Node(list_chars[char_index])
                    tmp_node.prev = prev_node
                    prev_node.next = tmp_node
                    prev_node = prev_node.next

            elif index > 1:
                key, val = line.rstrip("\n").split(' -> ')
                char_map[key] = val

    return initial_list, char_map


def add_char(node: Node, val: str) -> None:
    prev_node = node.prev
    new_node = Node(val)
    new_node.next = node
    new_node.prev = prev_node
    prev_node.next = new_node
    node.prev = new_node


def print_list(initial_list: LinkedList):
    cur_node = initial_list.head
    result = ''
    while cur_node:
        result += cur_node.val
        cur_node = cur_node.next

    print(result)


def make_step(initial_list: LinkedList, char_map: {str: str}) -> LinkedList:
    cur_node = initial_list.head.next

    while cur_node:
        key = cur_node.prev.val + cur_node.val
        if key in char_map:
            add_char(cur_node, char_map[key])

        cur_node = cur_node.next

    # print_list(initial_list)

    return initial_list


def solution_part(filename: str, steps) -> int:
    initial_list, char_map = read_input(filename)
    # print_list(initial_list)
    while steps:
        initial_list = make_step(initial_list, char_map)
        steps -= 1

    counter = {}

    cur_node = initial_list.head
    while cur_node:
        if cur_node.val in counter:
            counter[cur_node.val] += 1
        else:
            counter[cur_node.val] = 1

        cur_node = cur_node.next

    return max(counter.values()) - min(counter.values())


assert (solution_part('input/day14.test.txt', 10) == 1588)
print('Result Part 1: ', solution_part('input/day14.txt', 10))

assert (solution_part('input/day14.test.txt', 40) == 2188189693529)
print('Result Part 2: ', solution_part('input/day14.txt', 40))
