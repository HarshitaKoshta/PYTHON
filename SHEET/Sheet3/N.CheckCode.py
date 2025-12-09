a,b = map(int, input().split())
s = input()

if(a+b+1 != len(s)):
    print("No")
else:
    if s[a] != '-':
        print("No")         
    else:
        valid = True
        for i in range(len(s)):
            if i != a and not s[i].isdigit():
                valid = False
                break
        
        print("Yes" if valid else "No")