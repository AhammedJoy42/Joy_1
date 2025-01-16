# set = collection which is unordered, unindexed . No duplicate values

utensils = {"fork", "spoon", "knife"};
dishes = {"bowl", "plate", "cup", "knife"};

print(len(utensils));
# utensils.add("napkin");
# utensils.remove("fork");
#utensils.clear();
dishes.update(utensils);
print(utensils);
print(dishes);
print(type(utensils));
print(type(dishes));

dinner_table1 = utensils.union(dishes);
dinner_table2 = dishes.union(utensils);
# for i in utensils:
#     print(i);
# for j in dishes:
#     print(j);

print(dinner_table1);
print(dinner_table2);
print(dishes.difference(utensils));
print(utensils.difference(dishes));
print(dishes.intersection(utensils));
print(utensils.intersection(dishes));