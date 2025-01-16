# Higher Order Function = a function either:
#                         1. accepts a function as an argument
#                            or
#                         2. returns a function
#                         (In Python, functions are also treated as objects)

def loud(text):
    return text.upper();
def quiet(text):
    return text.lower();

def hello(func):
    text = func("Hi!");
    print(text);

hello(loud);
hello(quiet);
