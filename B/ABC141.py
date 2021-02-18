s = input()
k = ["R", "U", "D"]
g = ["L", "U", "D"]
t = 0
for i in range(len(s)):
    if i % 2 == 0:
        if not(s[i] in k):
            t += 1
    else:
        if not(s[i] in g):
            t += 1
if t == 0:
    print("Yes")
else:
    print("No")
