n = int(input())



for products in range(1, n + 1):
    price = float(input())

    new_price = price - price * 65/100

    print(f'{new_price:.2f}')