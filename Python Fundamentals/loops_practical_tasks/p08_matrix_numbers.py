n = int(input())
j = 1
for row in range(1, n + 1):

    for cow in range(j, n + 1):
        print(cow, end=" ")
    j += 1
    n += 1

    print()


