
def greet_user():
    print("Hello!");
greet_user();
#
def greet_user1(name):
    print(f"Hello!, {name}");
greet_user1("Joy");
greet_user1("Jewel");
#
def describe_pet(name, type):
    print(f"I have an animal: {name}");
    print(f"It is: {type}");
describe_pet("Cat", "Faithful");
describe_pet("Dog", "Barks");
describe_pet("Lion", "Beast");
#
def describe_pet(name, type):
    print(f"I have an animal: {name}");
    print(f"My {name}'s name is: {type}");
describe_pet("Cat", "Tommy");
#
def describe_pet(name, type):
    print(f"I have an animal: {name}");
    print(f"My {name}'s name is: {type.title()}");
describe_pet("Cat", "Tommy");
#
def describe_pet(type = "Dog", name = "Tommy"):
    print(f"I have an animal: {type}");
    print(f"My {type}'s name is: {name.title()}");
describe_pet();
print(type(describe_pet()));
#
def get_formatted_name(first_name, last_name):
    #full_name = f"{first_name} {last_name}";
    full_name = first_name + last_name;
    return full_name.title();
n = get_formatted_name("Jewel ", "Joy");
print(n);
