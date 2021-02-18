n = int(input())
tls = list(map(int, input().split()))
ls = tls[:]
for i in range(1, n):
    ls[i] *= ls[i-1]
m = ls[-1]
t = 0
for i in range(n):
    t += int(m/tls[i])
print(m/t)
