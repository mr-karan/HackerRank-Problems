import re

def find(pat,text):
	match=re.search(pat,text)
	if match and len(text)==10:
		print 'YES'
	else:
		print 'NO'


nums=int(raw_input())
list=[]

for i in range(nums):
	phone=(raw_input())
	list.append(phone)

for j in (list):
	find(r'[7-9]\d{9}',(j))
