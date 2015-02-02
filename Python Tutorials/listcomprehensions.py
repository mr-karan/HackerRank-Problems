x=input()
y=input()
z=input()
n=input()
X=range(x+1)
Y=range(y+1)
Z=range(z+1)
total=[]

i=[]
for xi in X:
	for yi in Y:
		for zi in Z:
			if xi+yi+zi!=n:
				h=[xi,yi,zi]
				total.append(h)

print total


			