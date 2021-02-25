n, k = map(int, input().split())
ls = [0 for i in range(n)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        ls[j-1] += 1
ans = 0
for i in ls:
    if i == 0:
        ans += 1
print(ans)
