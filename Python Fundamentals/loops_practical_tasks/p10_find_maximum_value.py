import sys

n = int(input())

max_num = - sys.maxsize


for num in range(1, n + 1):
    curr_num = int(input())

    if curr_num > max_num:
        max_num = curr_num
print(max_num)