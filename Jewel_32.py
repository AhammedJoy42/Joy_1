# Lambda _ 3:

lambda num : num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))