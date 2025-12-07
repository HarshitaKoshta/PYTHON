N = input()

if '.' in N:
    i, d = N.split('.')
    
    if d.count('0') == len(d):
        print("int", int(i))
    else:
        print("float", int(i), "0." + d)
else:
    print("int", int(N))
