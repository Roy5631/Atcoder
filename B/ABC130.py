n, x = map(int, input().split())
ls = [0]+list(map(int, input().split()))
ans = -1
for i in range(1, n+1):
    ls[i] = ls[i]+ls[i-1]
    if ls[i] > x:
        ans = i
        break
if ans == -1:
    print(n+1)
else:
    print(ans)
