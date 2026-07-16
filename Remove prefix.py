#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    counts = 0
    for j in range(n-1,-1,-1):
        if a[j] in s:
            counts = j + 1
            break
        s.add(a[j])
    print(counts)   