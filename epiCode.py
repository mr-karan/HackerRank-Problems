"""invalues=map(int,raw_input().split(" "))
scorevalues=map(int,raw_input().split(" "))

n=invalues[0]
p=invalues[1]
x=invalues[2]
rating=[]

for i in range(n):
    rating.append(p*scorevalues[i])
    p=p-x

highest=max(rating)

print rating.index(highest)+1


n=input()
s=raw_input()
count=0
z=[s[i:i+j] for j in range(1,len(s)+1) for i in range(len(s)-j+1)]
for i in range(len(z)):
    if z[i][0]==z[i][-1]:
        count=count+1

print count
"""