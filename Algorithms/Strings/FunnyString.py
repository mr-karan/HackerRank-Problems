test=input()
for i in range(test):
    s=raw_input()
    r=s[::-1]
    diffs=[]
    diffr=[]
    for x in range(len(s)-1):
        y=x
        diffs.append(ord(s[x+1])-ord(s[y]))
    for a in range(len(r)-1):
        b=a
        diffr.append(abs((ord(r[a+1])-ord(r[b]))))
    
    if diffr==diffs:
        print "Funny"
    else:
        print "Not Funny"
        