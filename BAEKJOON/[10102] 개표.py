v = int(input())
vote = input()

cntA = 0
cntB = 0
for c in vote:
    if c == 'A':
        cntA += 1
    elif c == 'B':
        cntB += 1

if cntA > cntB:
    print("A")
elif cntA < cntB:
    print("B")
elif cntA == cntB:
    print("Tie")
