nums = [4, 42, 78, 1, 5];
print(nums);
nums.reverse();
print(nums);

nums.sort();
print(nums);
#nums.sort(reverse = True);
#print(nums);

print(sorted(nums, reverse = True));
print(nums);

numscopy = nums.copy();
mynums = list(nums);
mycopy = nums[:];

print(numscopy);
print(mynums);
print(mycopy);
print(nums);

mylist = list([1, "Neil", True]);
print(mylist);

# From Harry:
a = [1, 8, 7, 2, 21, 15];
print(a);
k = a.sort();
print(a);
r = a.reverse();
print(r);
print(a.append(9));
