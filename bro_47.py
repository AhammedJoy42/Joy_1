# sort() method = used with lists
# sort() function = used with iterables

students = ["Squidwaed", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"];
# students.sort(reverse=True);
# students.sort();
sorted_students = sorted(students);
for i in sorted_students:
    print(i);
print(students);

stu = [("Squidwaed", "F", 60),
       ("Sandy", "A", 33),
       ("Patrick", "D", 36),
       ("Spongebob", "B", 20),
       ("Mr.Krabs", "C", 78)]
grade = lambda grades : grades[1];
stu.sort(key=grade, reverse=True);
for k in stu:
    print(k);

age = lambda ages: ages[1];
stu.sort(key=age);
for m in stu:
    print(m);