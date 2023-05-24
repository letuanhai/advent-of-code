from itertools import combinations
from typing import List, Optional, Tuple

PREAMBLE_LEN = 25


def is_valid(num: int, prev_nums: List[int]) -> bool:
    sorted_prev_nums = sorted(prev_nums)
    if num <= sorted_prev_nums[0] or num > sum(sorted_prev_nums[-2:]):
        return False
    for pair in combinations(prev_nums, 2):
        if num == sum(pair):
            return True
    return False


def find_invalid_pos(nums: List[int]) -> Optional[int]:
    for i, num in enumerate(nums[PREAMBLE_LEN:]):
        if not is_valid(num, nums[i : i + PREAMBLE_LEN]):
            return i + PREAMBLE_LEN


def find_contiguous_set(nums: List[int], target: int) -> Tuple[int, int]:
    start, end = 0, 1
    for start in range(len(nums) - 1):
        end = start + 1
        while sum(nums[start:end]) < target:
            end += 1
        if sum(nums[start:end]) == target:
            break

    return start, end


def main():
    with open("d9/d9.txt", "r") as f:
        nums = [int(line.strip()) for line in f.readlines()]
    invalid_pos = find_invalid_pos(nums)
    if not invalid_pos:
        return
    start, end = find_contiguous_set(nums, nums[invalid_pos])
    print(max(nums[start:end]) + min(nums[start:end]))


if __name__ == "__main__":
    main()
