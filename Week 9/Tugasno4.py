def odds(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count

numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_count = odds(numbers_list)
print(f"There are {odd_count} odd numbers in the list.")