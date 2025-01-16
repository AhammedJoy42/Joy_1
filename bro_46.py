# Lambda function = function written in 1 line using Lambda function
#              accepts any number of arguments, but only has one expression.
#              (think of it as a shortcut)
#             (useful if needed for a short period of time, throw-away)
# lambda parameters : expression

def double(x):
    return x * 2;

print(double(5));
# 1
k = lambda x : x*2;
print(k(2));
# 2
multiply = lambda x,y : x*y;
print(multiply(2,3));
# 3
add = lambda a,b,c : a+b+c;
print(add(2,3,4));
# 4
full_name = lambda first_name,last_name : first_name + " " + last_name;
print(full_name("Jewel", "Joy"));
# 5
age_check = lambda age : True if age >= 18 else False;
print(age_check(19));

