#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sorted(a)
    x = 0
    y = len(a) - 1
    p = s[y]
    q = s[x] + s[x + 1]
    y -= 1
    x += 2
    while x < y:
        p += s[y]
        q += s[x]
        x += 1
        y -= 1
    if p > q:
        print("YES")
    else:
        print("NO")