from itertools import groupby
import math
import operator


def parse_input(raw):
    return sorted(int(n) for n in raw.splitlines())


with open("d10/d10.txt") as file:
    input10 = parse_input(file.read())


def get_differences(joltages):
    return list(map(operator.sub, joltages + [joltages[-1] + 3], [0] + joltages))


def multiply_diffs(differences):
    return differences.count(1) * differences.count(3)


def count_arrangements(differences):
    # this approach relies on the assumption that diffs are only 1 or 3
    # although the problem description says that diff could be 1, 2, 3
    return math.prod(
        (2 ** (len(m) - 1)) - (len(m) == 4)
        for k, g in groupby(differences)
        if k == 1 and len((m := list(g))) > 1
    )


differences = get_differences(input10)
answer1 = multiply_diffs(differences)
answer2 = count_arrangements(differences)
print(answer2)
