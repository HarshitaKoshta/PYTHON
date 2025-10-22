rows = int(input("Enter number of rows: "))

for i in range(rows):
    n = 1
    for j in range(i + 1):
        print(n,end=" ")
        n = n*(i - j)//(j + 1)  
    print()
