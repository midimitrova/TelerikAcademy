number_half_liter_bottle = int(input())
number_one_liter_bottle = int(input())

half_liter_bottle = 0.1
one_liter_bottle = 0.25

price = number_half_liter_bottle * half_liter_bottle + number_one_liter_bottle * one_liter_bottle
print(f'{price:.2f}')