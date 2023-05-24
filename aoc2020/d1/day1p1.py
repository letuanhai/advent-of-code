# coding: utf-8
with open("./day1.txt", "r") as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]

for i, num in enumerate(nums):
    for j, num2 in enumerate(nums[i:]):
        if num + num2 == 2020:
            print(num * num2)
            break
