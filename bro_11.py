#slicing = create a substring by extracting elements from another string indexing[] or slice()
#          [start:stop:step]

name = "Jewel Ahammed Joy";
first_name1 = name[0:5];
first_name2 = name[:5];
last_name1 = name[14:17];
last_name2 = name[14:];
funky_name = name[::7]
reversed_name = name[::-1];


print(first_name1);
print(first_name2);
print(last_name1);
print(last_name2);
print(funky_name);
print(reversed_name);

website = "http://google.com"
part = slice(7,13);
print(website[part]);