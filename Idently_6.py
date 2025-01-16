
while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print(f'Hi there! How can I help you?');
    elif user_input in ["bye", "see you"]:
        print(f'Goodbye! Have a great day!');
    elif user_input in ["+ ", "add"]:
        print(f"Sure! Let's do some addition! Please enter two numbers.")
        try:
                num1 = float(input("First Number: "));
                num1 = float(input("Second Number: "));
                print(f'The sum is {num1 + num2}')
        except ValueError:
                print(f"Oops! That doesn't seem like a valid number. Try again!");
    else:
        print(f"I'm sorry, I don't understand. Please try again.");

