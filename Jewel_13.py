# Sets
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
k = {1, 2, 2, 3}
print(k)

# True is dupe of 1, False is a dupe of Zero
n = {True, 2, False, 3, 4, 0}
print(n)

# Check if a value is in a set or not:
print(2 in k)
print(5 in k)

# But you cannot refer to an element in the set with an index position or a key

# Add a new element to a set:
k.add(8)
print(k)

# Add elements from one set to aonther:
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictonaries also

# Merge two sets to create a new set:
one = {1, 2, 3}
two = {3, 4, 5, 6}
newset = one.union(two)
print(newset)

# Keep only the duplicates:
one1 = {1, 2, 3}
two2 = {3, 4, 5, 6}
f = one1.intersection(two2)
print(f)
one.intersection_update(two)
print(one)

# Keep everything except the duplicates:
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
