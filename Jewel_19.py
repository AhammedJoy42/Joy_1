# Function _ 2:
def sum(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2
total = sum(1,"a")
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items("Dave", "John", "Sara")    

def mult_named_items(**aargos):
    print(aargos)
    print(type(aargos))
mult_named_items(first = "Dave", last = "Gray")