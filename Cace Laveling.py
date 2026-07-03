#flenbar
t = int(input())
for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pre_sum = a[0]
    smallest = a[0]
    result = [smallest]
    for i in range(1, n):
        pre_sum += a[i]
        current_average = pre_sum // (i + 1)
        if current_average < smallest:
            smallest = current_average
        result.append(smallest)

    print(*result)