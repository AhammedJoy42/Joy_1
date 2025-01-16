# Loop Control Statement = change a loops execution from its normal sequence
#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ");
#     if name != "":
#         break;


phone_number = "123-456-7890";
for i in phone_number:
    if i == "-":
        continue;
    print(i, end="");

for k in range(0, 21):
    if k == 13:
        pass
    print(k);