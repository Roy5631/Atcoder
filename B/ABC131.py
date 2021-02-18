n, l = map(int, input().split())
if n % 2 == 0:
    s = int((2*l+n-1)*(n//2))
else:
    s = int((2*l+n-1)*(n//2))+(l+(n//2))
ls = []
for i in range(n):
    if l+i >= 0:
        ls.append([abs(l+i), 1])
    else:
        ls.append([abs(l+i), -1])
ls = sorted(ls, key=lambda x: x[0])
print(s-ls[0][1]*ls[0][0])
