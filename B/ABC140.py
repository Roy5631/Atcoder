n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
p = b[a[0]-1]
for i in range(1, n):
    t = a[i]-1
    p += b[t]
    if a[i-1] == a[i]-1:
        p += c[t-1]
print(p)
