#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = input().split()
    b = input().split()
    c = input().split()
    d = a + b + c 
    freq = {}
    for j in d:
        if j in freq:
            freq[j] += 1
        else:
            freq[j] = 1
    score1 = 0
    score2 = 0
    score3 = 0
    for j in a:
        if freq[j] == 1:
            score1 += 3
        elif freq[j] == 2:
            score1 += 1
    for j in b:
        if freq[j] == 1:
            score2 += 3
        elif freq[j] == 2:
            score2 += 1
    for j in c:
        if freq[j] == 1:
            score3 += 3
        elif freq[j] == 2:
            score3 += 1
    print(score1, score2, score3)
