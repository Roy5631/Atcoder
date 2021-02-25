x = int(input())
ans = int(100)
t = int(0)
while ans < x:
    ans = int(ans+ans//100)
    t += 1
print(t)
