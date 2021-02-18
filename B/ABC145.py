n = int(input())
s = list(input())
li = len(s)
if li % 2 == 0:
    p = int(li/2)
    if s[:p] == s[p:]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
