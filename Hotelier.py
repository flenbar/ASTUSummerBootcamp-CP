#flenbar
t = int(input())
s = input()
lists = [0] * 10
left = 0
right = 9
for i in range(t):
    if s[i] == "L":
        for j in range(10):
            if lists[j] == 0:
                lists[j] = 1
                break
    elif s[i] == "R":
        for j in range(9, -1, -1):
            if lists[j] == 0:
                lists[j] = 1
                break
    else:
        lists[int(s[i])] = 0
final = "".join(map(str, lists))
print(final)