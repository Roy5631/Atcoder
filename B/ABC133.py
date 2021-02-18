import math
n, d = map(int, input().split())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))
t = 0
for i in range(n-1):
    for j in range(i+1, n):
        h = 0
        for k in range(d):
            h += (ls[i][k]-ls[j][k])**2
        h = math.sqrt(h)
        h = h-math.floor(h)
        if h > 0:
            t = t
        else:
            t += 1
print(t)
