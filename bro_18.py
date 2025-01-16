# List = used to store multiple items in a single variable

food = ["pizza", "BURGER", "hotdog", "spaghetti", "pudding"];
for x in food:
    print(x);
print(food);
food[0] = "sushi";

print(food);
print(food[0]);
print(food[4]);
print(len(food));
food.remove("BURGER");
print(food);
food.insert(0, "cake");
food.sort();
#food.clear();
print(food);



