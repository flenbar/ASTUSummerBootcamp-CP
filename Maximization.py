#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = []
    y = []
    for j in range(n):
        if a[j] in x :
            y.append(a[j])
        else:
            x.append(a[j])
    x.sort()
    y.sort()
    z = x + y
    print(*z)
