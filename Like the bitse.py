#flenbar
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    counts = 0
    ok = True
    for ch in s:
        if ch == '1':
            counts += 1
            if counts >= k:
                ok = False
                break
        else:
            counts = 0
    if not ok:
        print("NO")
        continue
    print("YES")
    ones = []
    zeros = []
    for j in range(n):
        if s[j] == '1':
            ones.append(j)
        else:
            zeros.append(j)
    result = [0] * n
    value = 1
    for i in ones:
        result[i] = value
        value += 1
    for i in zeros:
        result[i] = value
        value += 1

    print(*result)     