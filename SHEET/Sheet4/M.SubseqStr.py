s = input().strip()
target = "hello"

j = 0

for ch in s:
    if ch == target[j]:
        j += 1
        if j == 5:
            break

if j == 5:
    print("YES")
else:
    print("NO")
