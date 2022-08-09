d = int(input())
h = int(input())
m = int(input())
s = int(input())


s_from_d = d * 24 * 60 * 60
s_from_h = h * 60 * 60
s_from_m = m * 60

total_seconds = s_from_d + s_from_h +s_from_m + s
print(total_seconds)

