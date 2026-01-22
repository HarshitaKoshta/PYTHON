def concatenate_arrays(A, B):
    C = B + A   
    return C

N = int(input())                
A = list(map(int, input().split()))  
B = list(map(int, input().split()))  

C = concatenate_arrays(A, B)

print(*C)
