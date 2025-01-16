
name = "Joy";
age = 22;
print(name, age);
print(f"Hello! My name is {name}. I am age {age} years old.")

a = "Eleven";
print(a);

from typing import Final

VERSION: Final[str] = "1.0.12";
PI: Final[float] = 3.1415

# Effective Python:
from datetime import datetime
k = datetime.now();
print("This is the current time: ", k);
print(f"This is the current time: {k}");
# Using Function:
def show_date():
    print(f"This is the current date and time: ");
    print(datetime.now());
show_date();
show_date();

# Greeting Function:
def greet(name):
    print(f"Hello! {name}");
greet("Joy");
greet("Nabila");