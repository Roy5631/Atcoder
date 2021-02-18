n = int(input())
ls = list(map(int, input().split()))
p = 0
for i in range(1, n+1):
    if ls[i-1] != i:
        p += 1
if p == 0 or p == 2:
    print("YES")
else:
    print("NO")
