#flenbar
t = int(input())
for k in range(t):
    n, m, k = map(int, input().split())
    a = list(input().strip())
    b = list(input().strip())
    a.sort()
    b.sort()
    i = 0
    j = 0
    ca = 0
    cb = 0
    Down = []
    while i < n and j < m:
        if (a[i] < b[j] and ca < k) or cb == k:
            Down.append(a[i])
            i += 1
            ca += 1
            cb = 0
        else:
            Down.append(b[j])
            j += 1
            cb += 1
            ca = 0
    print("".join(Down))