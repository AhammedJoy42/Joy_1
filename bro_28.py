# Scope = The region that a variable is recognised
#    A variable is only available from inside the region it is created.
#    A global and locally scoped version of a variable can be created

name = "Bro"; # global scope (Available inside & outside functions)

def display_name():
    name = "Code";   # Local scope(available only inside this function)
    print(name);

display_name();
print(name);
