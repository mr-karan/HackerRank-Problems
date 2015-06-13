import math

numTest=input()
for i in range(numTest):
	count=0
	numrange=map(int,raw_input().split(" "))
	for x in range(numrange[0],numrange[1]+1):
		if math.sqrt(x).is_integer():
			count=count+1
	print count



'''Alternate Approach is to compute math.floor(math.sqrt(numrange[1])) - math.ceil(math.sqrt(numrange[0])) + 1  ,because the above
solution exceeds the Time Limit. This one is perfect O(1) solution..
'''
'''Another solution is that we can simply take √a and √b and count the numbers between them using
⌊√b⌋−⌈√a⌉+1
 '''




