
age: int = 10;
name: str = "Bob";
print(age);
print(name);
print("Name : " + name + ",\nAge : " + str(age));

print(f'Name: {name}, Age: {age}');

# FUNCTION:

def add(a, b):
    print(f'Adding : {a} + {b}');
    c = a + b;
    return c;
k = add(3,5);
print(k);

#

def func() -> None:
    print("Hello");
func();
func();
func();

















