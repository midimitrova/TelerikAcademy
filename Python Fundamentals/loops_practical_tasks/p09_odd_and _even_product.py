n = int(input())

sum_even = 1
sum_odd = 1

for num in range(1, n + 1):
    curr_nums = int(input())

    if num % 2 == 0:
        sum_even *= curr_nums
    else:
        sum_odd *= curr_nums

if sum_even == sum_odd:
    print(f"yes {sum_even}")
else:
    print(f"no {sum_odd} {sum_even}")