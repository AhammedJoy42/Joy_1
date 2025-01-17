# Literal assignment

first = "Dave";
last = "Gray";
print(type(first));
print(type(first) == str);
print(isinstance(first, str));

# Concatenation
fullname = first + " " + last;
print(fullname);
fullname += "!";
print(fullname);

# Constructor Function
pizza = ("Pepperoni");
print(type(pizza));
print(type(pizza) == str);
print(isinstance(pizza, str));

# Casting a Number to String
decade = str(1980);
print(decade);
print(type(decade));

statement = "I like rock music from the " + decade + "s";
print(statement);

# Multiple Line
multLine = '''
Hey, how are you?

I was just checking in.
                       All Good?
'''
print(multLine);

# Escaping Special Characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\location";
print(sentence);