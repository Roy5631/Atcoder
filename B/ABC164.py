a, b, c, d = map(int, input().split())
x = 0
while a > 0 and c > 0:
    c -= b
    if c <= 0:
        x = 1
        break
    a -= d
    if a <= 0:
        x = -1
        break
if x == 1:
    print("Yes")
elif x == -1:
    print("No")
else:
    print(0)
