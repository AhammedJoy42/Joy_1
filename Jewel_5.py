# Build a Menu

title = "menu".upper();
print(title.center(20, "="));
print("Coffee".ljust(16, ".") + "$1".rjust(4));
print("Muffin".ljust(16, ".") + "$2".rjust(4));
print("CheeseCake".ljust(16, ".") + "$4".rjust(4, "+"));

# String Index Values
first = "dave";
print(len(first));
print(first[0]);
print(first[-1]);
print(first[1:]);
print(first[1:-1]);

#Some methods return Boolean data
print(first.startswith("D"));
print(first.startswith("d"));
print(first.endswith("z"));

#Boolean data Type
myvalue = True;
x = bool(False);
print(type(x));
print(isinstance(myvalue, bool));
print(isinstance(x, bool));