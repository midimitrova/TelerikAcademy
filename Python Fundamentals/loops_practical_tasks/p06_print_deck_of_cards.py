n = input()

suits = ('spades', 'clubs', 'hearts', 'diamonds')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'J':11,
         'Q':12, 'K':13, 'A':14}

if n == 'J':
    n = 11
elif n == 'Q':
    n = 12
elif n == "K":
    n = 13
elif n == "A":
    n = 14

n = int(n)

for rank in ranks:
    print(rank + ' of ' + 'spades,', rank + ' of ' + 'clubs,', rank + ' of ' + 'hearts,', rank + ' of ' + 'diamonds')
    if int(n) == 2:
        break
    n -= 1
