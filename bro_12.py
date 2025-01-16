# if statement = a block of code that will execute if it's condition is true:

age = int(input("Enter your age: "));

if age == 100:
    print("You're a century old!");
elif age >= 18:
    print("You're an adult!");
elif age < 0:
    print("You haven't born yet!");
else:
    print("You're a child!");
