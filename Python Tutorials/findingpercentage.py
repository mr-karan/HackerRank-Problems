students=int(raw_input())
a={}
for i in range(students):
	details=raw_input()
	dlist=details.split()
	name=dlist[0]
	dintlist=map(float,dlist[1:])
	a[name]=dintlist

#print a.items()

user=raw_input()

needed=a.get(user)

if needed==None:
	print 'not found'

z=sum(needed)/float(len(needed))

print("%.2f" %z)