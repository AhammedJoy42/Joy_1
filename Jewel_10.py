# Tuples

mytuple = tuple(("Dave", 42, True));
anothertuple = (1,4,2,8,2,2);
print(mytuple);
print(anothertuple);
print(type(mytuple));
print(type(anothertuple));

newlist = list(mytuple);
newlist.append("Neil");
newtuple = tuple(newlist);
print(newtuple);

(one, *two, hey) = anothertuple
print(one);
print(two);
print(hey);

print(anothertuple.count(2));

a = (1, 7, 2, 4);
print(a);
print(a.count(1));
print(a.index(2));
