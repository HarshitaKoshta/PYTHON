N,M = map(int,input().split())
N = int(N)
M = int(M)

if(N>9):
    N= N%10
if(M>9):
    M= M%10

print(N+M)        