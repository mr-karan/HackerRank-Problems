from collections import defaultdict
test_case=list(map(int,input().split(" ")))
n=test_case[0]
m=test_case[1]
l=defaultdict(list)
for i in range(1,n+1):
    sysin=input()
    l[sysin].append(i)

mlist=[]
for i in range(m):
    sysin=input()
    mlist.append(sysin)
    

for i in range(len(mlist)):
    if mlist[i] in l.keys():
        print(" ".join(str(x) for x in l.get(mlist[i])))
    else:
        print("-1")
