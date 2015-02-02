def cube(x):
	return x**3

def fib(n):
    list=[]
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
max=int(raw_input())
list=[]
for i in range(max):
    list.append(fib(i))

list=map(cube ,list)

print list