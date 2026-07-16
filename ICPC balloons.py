#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    se = list(set(s))
    total = len(se)*2 + ( n - len(se))
    print(total)