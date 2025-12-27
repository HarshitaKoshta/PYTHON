n = int(input())
s = input()

freq = [0]*26

for i in s:
    freq[ord(i)-97] += 1

ans = ""
for i in range(26):
    ans += chr(i+97) * freq[i]

print(ans)