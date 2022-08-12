import  sys

n = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize
sum = 0

for num in range(1, n + 1):
    curr_num = float(input())
    sum += curr_num

    if curr_num > max_num:
        max_num = curr_num
    if curr_num < min_num:
        min_num = curr_num

average_sum = sum / n

print(f'min={min_num:.2f}')
print(f'max={max_num:.2f}')
print(f'sum={sum:.2f}')
print(f'avg={average_sum:.2f}')

