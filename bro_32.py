import random

x = random.randint(1, 6);
y = random.random();
myList = ["rock", "paper", "scissors"];
z = random.choice(myList);

print(x);
print(y);
print(z);

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A"];
random.shuffle(cards);
print(cards);
