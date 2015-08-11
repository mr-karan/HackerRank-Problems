invalues=map(int,raw_input().split(" "))
scorevalues=map(int,raw_input().split(" "))

n=invalues[0]
p=invalues[1]
x=invalues[2]
rating=[]

for i in range(n):
    rating.append(p*scorevalues[i])
    p=p-x

print rating
