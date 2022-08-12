
n = int(input())

num_list = []


for num in range(1, n + 1):
    curr_num = int(input())

    num_list.append(curr_num)

num_list.sort()
num_list = num_list[::-1]

print(f'{num_list[0]}, {num_list[1]} and {num_list[2]}')
