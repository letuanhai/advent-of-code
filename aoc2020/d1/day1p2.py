# coding: utf-8
from itertools import combinations
from functools import reduce

with open("./day1.txt", "r") as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]

all_combinations = combinations(nums, r=3)
combo = list(filter(lambda nums: sum(nums) == 2020, all_combinations))
print(reduce(lambda x, y: x*y, combo[0], 1))
