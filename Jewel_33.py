# Lambda _ 4:


numbers = [3, 7, 12, 18, 20, 21]

lambda num : num % 2 != 0

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))