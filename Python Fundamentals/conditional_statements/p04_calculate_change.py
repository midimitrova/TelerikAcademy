price = float(input())
sum_paid = int(input())

sum_paid_st = sum_paid * 100
result = sum_paid_st - price * 100
coins_100 = 0
coins_50 = 0
coins_20 = 0
coins_10 = 0
coins_5 = 0
coins_2 = 0
coins_1 = 0

while result > 0:
    if result >= 100:
        result -= 100
        coins_100 += 1

    if 100 > result >= 50:
        result -= 50
        coins_50 += 1

    if 50 > result >= 20:
        result -= 20
        coins_20 += 1

    if 20 > result >= 10:
        result -= 10
        coins_10 += 1

    if 10 > result >= 5:
        result -= 5
        coins_5 += 1

    if 5 > result >= 2:
        result -= 2
        coins_2 += 1

    if 2 > result >= 1:
        result -= 1
        coins_1 += 1


if coins_100 != 0:
    print(f'{coins_100} x 1 lev')
if coins_50 != 0:
    print(f'{coins_50} x 50 stotinki')
if coins_20 != 0:
    print(f'{coins_20} x 20 stotinki')
if coins_10 != 0:
    print(f'{coins_10} x 10 stotinki')
if coins_5 != 0:
    print(f'{coins_5} x 5 stotinki')
if coins_2 != 0:
    print(f'{coins_2} x 2 stotinki')
if coins_1 != 0:
    print(f'{coins_1} x 1 stotinka')