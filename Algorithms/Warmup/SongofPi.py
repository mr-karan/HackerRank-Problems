import re
n = input()
for i in range(n):
    song = raw_input()
    matches = re.findall('\w+', song)
    pi = '31415926535897932384626433833'
    lengthsong = []
    for i in matches:
        lengthsong.append(len(i))

    lengthsongstr = ""
    lengthsongstr = lengthsongstr.join(map(str, lengthsong))

    digits = len(lengthsongstr)

    if pi[:digits] == lengthsongstr:
        print "It's a pi song."
    else:
        print "It's not a pi song."
