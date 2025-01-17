# String Methods

first = "Jewel";
print(first);
print(type(first));
print(first.upper());
print(first.lower());

multLine = '''
Hey, how are you?

I was just checking in.
                       All Good?
'''
print(multLine);
print(multLine.title());
print(multLine.replace("Good", "ok"));
print(multLine);

print(len(multLine));
multLine += "                  ";
multLine = "              " + multLine;
print(len(multLine));
print(multLine);
print(len(multLine.strip()));
print(len(multLine.lstrip()));
print(len(multLine.rstrip()));



