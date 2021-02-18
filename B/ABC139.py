a, b = map(int, input().split())
c = a-1
d = b-1
if d % c == 0:
    print(d//c)
else:
    print(d//c+1)
