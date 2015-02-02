N = int(raw_input())
li=[]
m=raw_input()
li=m.split(' ')
li=map(int,li)


a=set(li)
z=sorted(a)
print z[-2]
