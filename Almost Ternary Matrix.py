t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    for j in range(n):
        row = []
        for k in range(m):
            if ((j // 2) + (k // 2)) % 2 == 0:
                if (j + k) % 2 == 0:
                    row.append(1)
                else:
                    row.append(0)
            else:
                if (j + k) % 2 == 0:
                    row.append(0)
                else:
                    row.append(1)
        print(*row)
