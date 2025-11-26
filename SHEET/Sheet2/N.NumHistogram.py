s = input()
n  = int(input())

nums = list(map(int,input().split()))  

for x in nums:
    print(s * x)