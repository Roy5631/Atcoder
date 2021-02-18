n, d = map(int, input().split())
s = d*2+1
if n % s == 0:
    print(n//s)
else:
    print(n//s+1)
