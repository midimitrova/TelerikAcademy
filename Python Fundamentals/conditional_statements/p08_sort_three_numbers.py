
largest = 0
middle = 0
smallest = 0

first_num = int(input())
second_num = int(input())
third_num = int(input())

if first_num >= -1000 and first_num <= 1000 or second_num >= -1000 and second_num <= 1000 or third_num >= -1000 and third_num <= 1000:

    if first_num >= second_num and first_num >= third_num:
        largest = first_num
        if second_num >= third_num:
            middle = second_num
            smallest = third_num
        else:
            middle = third_num
            smallest = second_num
    elif second_num >= first_num and second_num >= third_num:
        largest = second_num
        if first_num >= third_num:
            middle = first_num
            smallest = third_num
        else:
            middle = third_num
            smallest = first_num
    elif third_num >= first_num and third_num >= second_num:
        largest = third_num
        if first_num >= second_num:
            middle = first_num
            smallest = second_num
        else:
            middle = second_num
            smallest = first_num
    elif first_num == second_num == third_num:
        largest = first_num
        middle = second_num
        smallest = third_num
print(largest, middle, smallest)

