
# Open & read a file:
try:
    with open('test.txt') as file:
        print(file.read());

except FileNotFoundError:
    print("Something is wrong!");