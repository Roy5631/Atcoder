n, a, b = map(int, input().split())
p = n % (a+b)
q = n//(a+b)
if 0 <= p <= a:
    print(q*a+p)
else:
    print(q*a+a)
