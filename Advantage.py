#flenbar
t = int(input())
for i in range(t) :
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a)
    for j in range(n):
        if a[j] != b[-1]:
            a[j] -=  b[-1]
        else:
            a[j] -= b[-2]
    print(*a)        