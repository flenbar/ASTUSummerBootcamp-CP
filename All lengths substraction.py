#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    left = 0
    right = n - 1
    check = True
    for j in range(1, n + 1):
        if left <= right and p[left] == j:
            left += 1
        elif left <= right and p[right] == j:
            right -= 1
        else:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")