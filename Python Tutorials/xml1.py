import xml.etree.ElementTree as etree

lines=int(raw_input())
xml=""
for i in range(lines):
    xml+=raw_input()



tree=etree.ElementTree(etree.fromstring(xml))

score=0

for j in tree.iter():
    score+=len(j.attrib)

print score

