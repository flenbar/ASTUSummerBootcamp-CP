t = int(input())
for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    occupied = set()
    occupied.add(a[0])
    ok = True
    for i in range(1, n):
        seat = a[i]
        if (seat - 1 not in occupied) and (seat + 1 not in occupied):
            ok = False
            break
 
        occupied.add(seat)
 
    if ok:
        print("YES")
    else:
        print("NO")
