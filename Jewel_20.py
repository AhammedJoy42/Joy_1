# Recursion _ 1:
def add_one(num):
    if(num >= 9):
        return num + 1
    
    total = num + 1
    print(total)
    
    add_one(total)
mynewtotal = add_one(0)
print(mynewtotal)
#
value = True
while value:
    print(value)
    value = 0