sum_deposit = int(input())

percentage = 0.05
first_year = percentage * sum_deposit + sum_deposit
second_year = first_year * percentage + first_year
third_year = second_year * percentage + second_year

print(f'{first_year:.2f}')
print(f'{second_year:.2f}')
print(f'{third_year:.2f}')