def sorter(a):
	new=[]
	for i in (a):
			if i[0]=='0':
				i=i[1:]
				new.append(i)
			elif i[0]=='+':
				i=i[3:]
				new.append(i)
			elif i[0]=='9' and i[1]=='1' and len(i)>10:
				i=i[2:]
				new.append(i)
			elif i[0]=='9' and i[1]=='1' and len(i)==10:
				new.append(i)
			else:
				new.append(i)
	new=sorted(new)
	for i in new:
		print '+91 '+i[:5]+' '+i[5:]


num=int(raw_input())
phone=[]
for i in range(num):
	a=raw_input()
	phone.append(a)

sorter(phone)