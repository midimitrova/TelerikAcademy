n = int(input())

sum = 0

for num in range(1, n + 1):
    curr_num = float(input())
    sum += curr_num

average_sum = sum / n
print(f'{average_sum:.2f}')
