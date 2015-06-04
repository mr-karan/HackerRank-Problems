t = input()
for i in range(t):
    inputstring = raw_input().split(' ')

    n = int(inputstring[0])
    k = int(inputstring[1])

    arrivaltime = raw_input().split(' ')
    arrivaltime = map(int, arrivaltime)
    counterLate = 0
    counterBefore = 0
    for i in arrivaltime:
        if i <= 0:
            counterBefore = counterBefore + 1
        elif i > 0:
            counterLate = counterLate + 1

    if counterBefore >= k:
        print "NO"
    elif counterBefore < k:
        print "YES"
