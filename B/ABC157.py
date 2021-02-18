bng = []
for i in range(3):
    bng.extend(list(map(int, input().split())))
n = int(input())
d = []
for i in range(n):
    b = int(input())
    for i in range(9):
        if bng[i] == b:
            d.append(i)
ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
t = 0
for i in range(len(ls)):
    p = 0
    for j in ls[i]:
        if j-1 in d:
            p += 1
    if p == 3:
        t += 1
        break
if t > 0:
    print("Yes")
else:
    print("No")
