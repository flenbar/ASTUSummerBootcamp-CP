#flenbar
a = int(input())
for b in range(a):
    c = int(input())
    d = input()
    e = []
    for f in range(c // 2):
        if d[f] != d[c - 1 - f]:
            e.append(f)
    if not e:
        print("Yes")
    else:
        g = True
        for h in range(1, len(e)):
            if e[h] != e[h - 1] + 1:
                g = False
                break
        if g:
            print("Yes")
        else:
            print("No")