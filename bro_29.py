#Args = parameter that will pack all arguments into a tuple
#      useful so that a function can accept a varying amount of arguments

def add1(*stuff):
    sum = 0;
    for i in stuff:
        sum += i;
    return sum;
print(add1(1,2,3,4,5,6));


def add2(*args):
    s = 0;
    args = list(args);
    args[0] = 0;
    for i in args:
        s += i;
    return s;
print(add2(1,2,3,4))