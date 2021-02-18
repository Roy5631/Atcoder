n = int(input())
p = list(map(int, input().split()))
m = 1000000
for i in range(n-1):
    s1 = sum(p[:i+1])
    s2 = sum(p[i+1:])
    tmp = abs(s1-s2)
    if tmp <= m:
        m = tmp
print(m)
