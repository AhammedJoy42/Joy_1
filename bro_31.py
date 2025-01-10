# str.format() = optional method that gives users
#               more controls when displaying output.

num = 1000;
print("The number pi is {:.3f}".format(num));
print("The number is {:,}".format(num));
print("The number is {:b}".format(num));
print("The number is {:o}".format(num));
print("The number is {:X}".format(num));
print("The number is {:E}".format(num));

animal = "cow";
item = "moon";
print("The " + animal + " jumped over the " + item);
print("The {} jumped over the {}".format(animal, item));
print("The {} jumped over the {}".format(item, animal));
print("The {0} jumped over the {1}".format(animal, item));  #positional argument
print("The {animal} jumped over the {item}".format(item="Sun", animal="dog"));  #keyword argument
print(text.format(animal, item));