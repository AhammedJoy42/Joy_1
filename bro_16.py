# nested Loop = The "inner Loop" will finish all of it's iteration before
#               finishing one iteration of the "outer Loop"

row = int(input("Enter the number of rows: "));
col = int(input("Enter the number of columns: "));
symbol = input("Enter a symbol to use: ")

for i in range(row):
    for j in range(col):
        print(symbol, end=" ")
    print()