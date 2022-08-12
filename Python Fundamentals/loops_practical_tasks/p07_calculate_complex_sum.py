n = int(input())
x = int(input())


def fact(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out

result = 1
for i in range(1, n+1):
    result += fact(i) / x**i
print(f'{result:.5f}')
