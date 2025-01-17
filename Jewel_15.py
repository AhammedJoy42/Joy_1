# Loops _ 2:
names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)    

for x in names:
    if x == "Sara":
        break
    print(x)

for x in names:
    if x == "Sara":
        continue
    print(x)