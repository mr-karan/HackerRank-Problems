n = input()


for i in range(n):
    numint = input()
    numlist = map(int, list(str(numint)))
    flag = 0
    for j in range(len(numlist)):
        if numlist[j] == 0:
            continue
        elif numint % (numlist[j]) == 0:
            flag += 1
    print flag
