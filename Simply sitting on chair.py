#flenbar
a = int(input())
for i in range(a):
    b = int(input())
    a = list(map(int,input().split()))
    counts = 0
    for j in range(b):
        if a[j] <= j+1:
            counts += 1
    print(counts)
