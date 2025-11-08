def vowel(s):
    vow = 'aeiou'
    count = 0
    for ch in s.lower():
        if ch in vow:
            count += 1
    return count

print(vowel('harshita'))