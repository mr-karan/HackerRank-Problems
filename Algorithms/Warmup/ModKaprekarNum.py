p = input()
q = input()

def even(n):
	if n%2==0:
		return True
	else:
		return False


flag = 0

for i in range(p, q + 1):

    digits = len(str(i))

    sqdigits=len(str(i**2))

    numlist = map(int, str(i**2))

    if not even(sqdigits):
    	left = numlist[:digits-1]
    	right = numlist[digits-1:]
    else:
    	left = numlist[:digits]
    	right = numlist[digits:]

    if len(left) != 0:
        lnum = int("".join(map(str, left)))
    else:
        lnum = 0

    if len(right) != 0:
        rnum = int("".join(map(str, right)))
    else:
        rnum = 0

    if lnum + rnum == i:
        print i
        flag = flag + 1
    else:
        continue

if flag == 0:
    print "INVALID RANGE"
