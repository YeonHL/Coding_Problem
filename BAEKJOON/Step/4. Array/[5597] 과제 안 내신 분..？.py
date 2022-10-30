_num = [0] * 31

for i in range(28):
    _num[int(input())] = 1

for i in range(1, 31):
    if _num[i] == 0:
        print(i)
