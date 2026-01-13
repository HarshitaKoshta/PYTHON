def calculate_average(arr):
    total = sum(arr)
    avg = total / len(arr)
    return avg

n = int(input().strip())
arr = list(map(float, input().split()))

result = calculate_average(arr)

print("{:.6f}".format(result))
