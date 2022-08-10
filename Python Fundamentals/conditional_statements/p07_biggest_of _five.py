import sys

max_num = -sys.maxsize

first_num = int(input())
second_num = int(input())
third_num = int(input())
fourth_num = int(input())
fifth_num = int(input())


if first_num > max_num:
    max_num = first_num
if second_num > max_num:
    max_num = second_num
if third_num > max_num:
    max_num = third_num
if fourth_num > max_num:
    max_num = fourth_num
if fifth_num > max_num:
    max_num = fifth_num

print(max_num)