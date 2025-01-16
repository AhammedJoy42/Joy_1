
# Open & write a file:

text = "Uh No.\n This is some text.\n Have a good one!\n";

with open('test.txt', 'w') as file:
    file.write(text);