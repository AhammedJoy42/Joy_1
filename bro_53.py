# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets etc..)
#            creats a zip object with paired elements stored in tuples for each elements.

usernames = ["Dude", "Bro", "Mister"];
passwords = ("p@ssword", "abc123", "guest");
users = dict(zip(usernames, passwords))
print(type(users));
print(users);

k = zip(usernames, passwords);
for i in k:
    print(k);
print(type(k));