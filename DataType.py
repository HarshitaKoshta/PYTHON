n, k, a = map(int, input().split())

val = n * (k ** a)

INT_MIN, INT_MAX = -2147483648, 2147483647
LL_MIN, LL_MAX = -9223372036854775808, 9223372036854775807

if INT_MIN <= val <= INT_MAX:
    print("int")
elif LL_MIN <= val <= LL_MAX:
    print("long long")
else:
    print("double")
