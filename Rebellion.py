#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    left = 0
    right = n - 1
    res = 0
    while True:
        while left < n and a[left] == 0:
            left += 1
        while right >= 0 and a[right] == 1:
            right -= 1
        if left >= right:
            break
        res += 1
        left += 1
        right -= 1
    print(res)