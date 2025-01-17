# f-Strings _ 2

player = {"person" : "Dave", "coins" : 3}
person = "Dave"
coins = 3
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.upper()} has {2 * 5} coins left."
print(message)

message = f"\n{player["person"]} has {2 * 5} coins left."
print(message)