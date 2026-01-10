def findminmax(arr):
    return min(arr), max(arr)

n = int(input())
arr = list(map(int, input().split()))

mn, mx = findminmax(arr)
print(mn, mx)
