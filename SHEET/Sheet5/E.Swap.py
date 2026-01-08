def swapp(x, y):
    return y, x

x, y = map(int, input().split())
x, y = swapp(x, y)
print(x, y)
