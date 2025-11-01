N = int(input())

for i in range(N):
    line = input().split()
    a = int(line[0][::-1]) 
    b = int(line[1][::-1])  

    sum = a + b                
    print(int(str(sum)[::-1]))