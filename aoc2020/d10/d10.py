from collections import Counter
from functools import lru_cache

with open("d10/d10.txt", "r") as f:
    nums = [int(line.strip()) for line in f.readlines()]

sorted_nums = sorted(nums)
sorted_nums = [0] + sorted_nums + [max(sorted_nums) + 3]

diffs = [sorted_nums[i + 1] - sorted_nums[i] for i in range(len(nums) - 1)]
c = Counter(diffs)
print(c)

l = len(sorted_nums)


@lru_cache
def count_path(i: int) -> int:
    if i == l - 1:
        return 1
    else:
        return sum(
            count_path(i + j)
            for j in range(1, 4)
            if (i + j < l) and (sorted_nums[i + j] - sorted_nums[i] <= 3)
        )


print(count_path(0))
