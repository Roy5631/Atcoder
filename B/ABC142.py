n, k = map(int, input().split())
h = list(map(int, input().split()))
t = 0
for i in h:
    if i >= k:
        t += 1
print(t)
