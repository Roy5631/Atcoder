n = int(input())
ls = sorted(map(int, input().split()))
ans = 0
for i in range(len(ls)-2):
    for j in range(i+1, len(ls)-1):
        for k in range(j+1, len(ls)):
            if ls[i]+ls[j] > ls[k] and ls[i] != ls[j] and ls[i] != ls[k] and ls[j] != ls[k]:
                ans += 1
print(ans)
