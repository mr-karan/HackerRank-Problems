# Enter your code here. Read input from STDIN. Print output to STDOUT

test=input()
cp=0.0
cn=0.0
cz=0.0
l=[]

for i in range(test):
    s=raw_input()
    l=map(int,s.split(" "))

    for i in l:
            if i>0:
                cp=cp+1
            elif i<0:
                cn=cn+1
            else:
                cz=cz+1

    print ("%.3f" % (cp/len(l)))
    print ("%.3f" % (cn/len(l)))
    print ("%.3f" % (cz/len(l)))