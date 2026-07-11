#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    value = True
    for j in range(1, n - 1, 2):
        if a[j] != a[j + 1]:
            value = False
            break
    if value :
        print("Yes")
        
    else :
        print("No")
    
