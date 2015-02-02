import re

def find(pat,text):
	match=re.search(pat,text)
	if match:
		return True
	else:
		return False


j=raw_input()
print find(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',(j))

