start_interval = int(input())
end_interval = int(input())
target_sum = int(input())

sum_num = 0

for d1 in range(0, 10):
    for d2 in range(0, 10):
        for d3 in range(0, 10):
            sum_num = (d1, d2, d3)
            my_num = f'{d1}{d2}{d3}'
            if sum(sum_num) == target_sum:
                if start_interval <= int(my_num) <= end_interval:
                    print(f'{d1}{d2}{d3}')
