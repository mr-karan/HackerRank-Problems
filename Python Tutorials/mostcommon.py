from collections import Counter

s=input()

ans=Counter(list(s)).most_common(3)

for k,v in ans:
    print (k,v)
