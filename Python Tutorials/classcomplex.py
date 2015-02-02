from math import *

class Complex(object):
	def __init__(self,real,imag):
		self.r=float(real)
		self.i=float(imag)

	def add(self,first,second):
		c.r=first.r+second.r
		c.i=first.i+second.i
		display(c.r,c.i)

	def sub(self,first,second):
		c.r=first.r-second.r
		c.i=first.i-second.i
		display(c.r,c.i)


	def mult(self,first,second):
		c.r=(first.r*second.r)-(first.i*second.i)
		c.i=(first.r*second.i)+(first.i*second.r)
		display(c.r,c.i)

	def div(self,first,second):
		c.r=((first.r*second.r)+(first.i*second.i))/((second.r)**2+(second.i)**2)
		c.i=((first.i*second.r)-(first.r*second.i))/(second.r**2+second.i**2)
		display(c.r,c.i)
	def mod(self):
		return sqrt(self.r**2+self.i**2)



def display(first,second):
	if c.r == 0 and c.i == 0:
		print('0.00')
	elif c.r == 0:
		print('{:.2f}i'.format(c.i))
	elif c.i == 0:
		print('{:.2f}'.format(c.r))
	else:
		print('{:.2f} {} {:.2f}i'.format(c.r, '-' if c.i < 0 else '+', abs(c.i)))


#a=Complex(2,1)
#b=Complex(5,6)
user1=map(float,raw_input().split(" "))
user2=map(float,raw_input().split(" "))





a=Complex(user1[0],user1[1])
b=Complex(user2[0],user2[1])
c=Complex(0,0)
c.add(a,b)
c.sub(a,b)
c.mult(a,b)
c.div(a,b)
print "%.2f"%(a.mod())
print "%.2f"%(b.mod())