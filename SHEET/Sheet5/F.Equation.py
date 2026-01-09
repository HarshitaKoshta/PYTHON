def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


def equation_sum(x, n):
    s = 0
    for i in range(0,n+1,2):
        if i == 0:
            s += power(x,0)-1
        else:
            s += power(x,i)
    return s


x, n = map(int, input().split())
print(equation_sum(x, n))
