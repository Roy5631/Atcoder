n = list(map(int, list(input())))
s = sum(n)
if s % 9 == 0:
    print("Yes")
else:
    print("No")
