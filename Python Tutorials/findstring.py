string1=raw_input()
substr=raw_input()
count=0

for i in range(len(string1)):
    if string1[i:i+len(substr)]==substr:
        count=count+1

print count