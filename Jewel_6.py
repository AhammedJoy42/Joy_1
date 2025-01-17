# Numeric Data Type

# Integer type
price = 100;
best_price = int(80);
print(price);
print(type(price));
print(best_price);
print(isinstance(best_price, int));

# float Type
gpa = 3.28;
y = float(1.14);
print(gpa);
print(type(gpa));
print(y);
print(isinstance(y, float));

# Complex Type
comp_value = 5 + 3j;
print(comp_value);
print(type(comp_value));
print(comp_value.real);
print(comp_value.imag);

# Build-in functions for numbers
print(abs(gpa));
print(abs(gpa * -1));
print(round(gpa));
print(round(gpa, 1));

import math
print(math.pi);
print(math.sqrt(64));
print(math.ceil(gpa));
print(math.floor(gpa));

# Casting a string to a number
zipcode = "10001";
zip_value = int(zipcode);
print(zipcode);
print(type(zipcode));
print(zip_value);
print(type(zip_value));

# Erroe: If you attempt to cast incorrect data
zip_value1 = int("New York");
print(zip_value_1);
