n = int(input())

for i in range(n):
    s = input()
    if(s.__contains__('010') or s.__contains__('101')):
        print("Good")
    else:
        print("Bad")

    