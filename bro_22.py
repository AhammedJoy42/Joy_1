# dictionary = A changeable, unordered collection of unique key:value paris
#              Fast because they use hashing, allow us to access a value quickly

capitals = {"USA" : "Washington DC",
            "Bangladesh" : "Dhaka",
            "China" : "Beijing",
            "Russia" : "Moscow"}

capitals.update({"Germany" : "Berlin"});
capitals.update({"USA" : "New York"});
capitals.pop("China");
#capitals.clear();

print(capitals["Germany"]);
print(capitals.get("Germany"));
for i in capitals:
    print(i);
print(capitals);

print(capitals.keys());
print(capitals.values());
print(capitals.items());

for key,value in capitals.items():
    print(key, value);