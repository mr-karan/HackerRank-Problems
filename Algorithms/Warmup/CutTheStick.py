'''
sticks-length        length-of-cut   sticks-cut
5 4 4 2 2 8             2               6
3 2 2 _ _ 6             2               4
1 _ _ _ _ 4             1               2
_ _ _ _ _ 3             3               1
_ _ _ _ _ _           DONE            DONE

'''
n = input()
sticks = map(int, raw_input().strip().split(" "))


sticks = sorted(sticks, reverse=True)
while(len(sticks) > 0):
    print len(sticks)
    leastnum = sticks.pop()
    while len(sticks) > 0 and sticks[-1] <= leastnum:
        sticks.pop()
