l = input()
r = input()

ans = []

for i in range(l, r):
    for j in range(l, r):
        ans.append(i ^ j)

ans = sorted(ans, reverse=True)

print ans[0]
