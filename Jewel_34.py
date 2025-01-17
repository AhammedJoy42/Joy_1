# Lambda _ 5:

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)
print(sum(numbers, 10))

lambda acc, curr : acc + len(curr)

names = ['Joy', 'Jewel', 'John Jacob']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)