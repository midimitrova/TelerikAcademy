command = input()

max_lenght = 0
food = ''

while command != 'END':
    if len(command) >= max_lenght:
        max_lenght = len(command)
        food = command

    command = input()
print(food)