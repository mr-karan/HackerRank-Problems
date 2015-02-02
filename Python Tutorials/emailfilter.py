

import re

pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

n = int(raw_input())
email = [ raw_input() for i in range(n) ]
final=[]
for i in email:
    if re.match(pattern,i):
        final.append(i)

print sorted(final)