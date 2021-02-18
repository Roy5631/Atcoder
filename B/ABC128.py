n = int(input())
ls = []
for i in range(n):
    a, b = input().split()
    ls.append([a, int(b), i+1])
ls = sorted(ls, key=lambda x: x[1])
ls = sorted(ls, key=lambda x: x[0])
for i in range(n):
    print(ls[i][2])
