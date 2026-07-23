#flenbar
t = int(input())
for i in range(t) :
    k , q = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    for j in range(q):
        print(min(b[j] , a[0]-1) , end=" ")
    print()    