s = input()

words = s.split()
count = 0

for w in words:
    for ch in w:
        if ch.isalpha():
            count += 1
            break

print(count)


# s = input()
# words = s.split()
# count = 0

# for w in words:
#     clean = ""
#     for ch in w:
#         if ch.isalpha():
#             clean += ch
#     if clean != "":
#         count += 1

# print(count)
