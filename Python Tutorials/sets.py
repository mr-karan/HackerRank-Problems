m=int(raw_input())
mint=raw_input()
mlis=mint.split()
mflis=map(int,mlis)

n=int(raw_input())
nint=raw_input()
nlis=nint.split()
nflis=map(int,nlis)


mset=set(mflis)
nset=set(nflis)

fset=mset.symmetric_difference(nset)
flist=[]
for j in fset:
	flist.append(j)

ans=sorted(flist)

for h in ans:
	print h