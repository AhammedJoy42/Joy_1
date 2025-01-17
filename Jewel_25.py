# f-Strings _ 1

person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left. ")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{person} has {coins} coins left."(person = person, coins = coins),
print(message)

message = "\n{1} has {0} coins left."#(person, coins)
print(message)

message = "\n{1} has {0} coins left."#(person, coins)
print(message)

player = {"person" : "Dave", "coins" : 3}
message = "\n{person} has {coins} coins left."
format(**player)
print(message)