
testcase = map(int, raw_input().strip().split(" "))
width = map(int, raw_input().strip().split(" "))

for x in range(testcase[1] + 1):

    segment = map(int, raw_input().strip().split(" "))

    allowed = []
    for i in range(segment[0], segment[1] + 1):
        allowed.append(width[i])

    print min(allowed)
