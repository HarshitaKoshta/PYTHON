def is_odd(n):
    return n % 2 == 1


def is_binary_palindrome(n):
    binary = bin(n)[2:]      # convert to binary without '0b'
    return binary == binary[::-1]


n = int(input())

if is_odd(n) and is_binary_palindrome(n):
    print("YES")
else:
    print("NO")
