#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    z = 0
    for j in range(n):
        x = s[j:] + s[:j]
        c = 1
        for k in range(1, n):
            if x[k] != x[k - 1]:
                c += 1
        if c > z:
            z = c
    print(z)