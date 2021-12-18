# https://adventofcode.com/2021/day/12


def read_input(filename) -> {str: set[str]}:
    graph = {}
    with open(filename) as file:
        for line in file.readlines():
            s, e = line.rstrip("\n").split("-")
            if s not in graph.keys():
                graph[s] = set()
            if e not in graph.keys():
                graph[e] = set()

            graph[s].add(e)
            graph[e].add(s)
    return graph


def solution_part1(filename: str) -> int:
    graph = read_input(filename)
    paths = set()

    def helper(node: set[str], path: str):
        for item in node:
            if item == 'end':
                path += ',end'
                paths.add(path)
            elif item.islower() and item not in path and item in graph.keys():
                helper(graph[item], path + ',' + item)
            elif item.isupper() and item in graph.keys():
                helper(graph[item], path + ',' + item)

    helper(graph['start'], 'start')

    return len(paths)


def solution_part2(filename: str) -> int:
    graph = read_input(filename)
    paths = set()

    def helper(node: set[str], path: str, small_cave_visited_twice: bool):

        if 'end' in path:
            paths.add(path)

        else:
            for item in node:
                if item == 'start':
                    pass
                elif item.islower() and path.count(item) == 0:
                    helper(graph[item], path + ',' + item, small_cave_visited_twice)
                elif item.islower() and path.count(item) == 1:
                    if not small_cave_visited_twice:
                        helper(graph[item], path + ',' + item, True)
                elif item.isupper():
                    helper(graph[item], path + ',' + item, small_cave_visited_twice)

    helper(graph['start'], 'start', False)

    return len(paths)


assert (solution_part1('input/day12.test.txt') == 10)
print('Result Part 1: ', solution_part1('input/day12.txt'))

assert (solution_part2('input/day12.test.txt') == 36)
print('Result Part 2: ', solution_part2('input/day12.txt'))
