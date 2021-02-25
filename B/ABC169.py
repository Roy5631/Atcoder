n = int(input())
ls = list(map(int, input().split()))
ls = sorted(ls)
if ls[0] == 0:
    print(0)
else:
    ans = 1
    t = 0
    for i in range(n):
        ans *= ls[i]
        if ans > 10**18:
            t = 1
            print(-1)
            break
    if t == 0:
        print(ans)
