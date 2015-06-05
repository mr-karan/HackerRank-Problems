n = input()
for i in range(n):
    z = list(raw_input().strip())
    count = 0
    for i in range(len(z) - 1, 0, -1):
        if z[::-1] == z:
            continue
        else:
            while(z[::-1] != z and ord(z[i]) > 97):
                z[i] = chr(ord(z[i]) - 1)

                count = count + 1
    print count
