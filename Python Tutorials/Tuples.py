n=input()
listNum=map(int,input().split(" ") )

tupleNum=tuple(listNum)

print (hash(tupleNum))
