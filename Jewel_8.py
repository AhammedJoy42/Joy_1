users = ["Dave", "John", "Sara"];
data = ["Dave", 42, True];
emptyList = []
print(users);
print(data);
print(emptyList);
print(type(users));

print("Dave" in users);
print("dave" in users);

print(users[1]);
print(users[-1]);

print(users.index("Sara"));
print(users[1:2]);
print(users[-3:-1]);

print(len(users));
print(len(data));
print(len(emptyList));

# users.append("Elsa");
# print(users);

users.extend(["Robert", "Jimmy"]);
print(users);

users += "Jason";
print(users);
users += ["Jason"];
print(users);

#users.extend(data);
#print(users);
users.insert(0, "Bob");
print(users);

users[2:2] = ["Eddie", "Alex"];
print(users);
users[1:3] = ["Robert", "JPJ"];
print(users);

users.remove("Bob");
print(users);

print(users.pop());
print(users);

del users[0];
print(users);

data.clear();
print(data);
print(data.clear());

users[1:2] = ["dave"];
users.sort();
print(users);

users.sort(key = str.lower);
print(users);