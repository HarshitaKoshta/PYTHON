n = int(input())
for k in range(n):
    S, T = input().split()
    
    i = 0
    result = ""

    while i < len(S) or i < len(T):
        if i < len(S):
            result += S[i]
        if i < len(T):
            result += T[i]
        i += 1

    print(result)
