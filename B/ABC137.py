k, x = map(int, input().split())
ans = ""
tmp = 0
for i in range(k):
    ans += str(x-k+1+i)
    tmp = x-k+1+i
    ans += " "
for i in range(1, k):
    ans += str(tmp+i)
    if i != k-1:
        ans += " "
print(ans)
