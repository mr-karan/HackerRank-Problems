from operator import itemgetter


def formatter(d):
	for i in d:
		if i[-1]=='M':
			print 'Mr. '+i[0]+' '+i[1]
		elif i[-1]=='F':
			print 'Ms. '+i[0]+' '+i[1]


n=int(raw_input())
d=[]
for i in range(n):
	a=raw_input()
 	d.append(a.split(' '))

d.sort(key=itemgetter(2))
formatter(d)

