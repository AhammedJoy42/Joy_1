# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("bro", 21, "joy", "bro");

print(student.count("bro"));
print(student.count("joy"));
print(type(student));
#print(student.index["joy"]);

print(len(student));
print(student[0]);
print(student[1]);
print(student[2]);
print(student[3]);


for x in student:
    print(x);

print(student);

if "joy" in student:
    print("Bro is here!");

#if "Belayet" in student:
    print("Belayet is not here!");


