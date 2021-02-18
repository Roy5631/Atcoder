n = int(input())
if n == 10**5:
    print(9+10**3-10**2+10**5-10**4)
else:
    ans = 0
    for i in range(5):
        if n < 10**(i+1):
            if i % 2 == 0:
                ans += n-10**(i)+1
            break
        else:
            if i % 2 == 0:
                ans += 10**(i+1)-10**(i)
    print(ans)
