label = input()
rank = int(input())

if label == 'b' or label == 'd' or label == 'f' or label == 'h':
    if rank % 2 != 0:
        print('light')
    else:
        print('dark')
else:
    if rank % 2 != 0:
        print('dark')
    else:
        print('light')
