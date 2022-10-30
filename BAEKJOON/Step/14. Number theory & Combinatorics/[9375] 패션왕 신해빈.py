# 각 부위의 개수 저장, 1개 고를 경우 각 부위의 개수의 합, 2개 고를 경우 부위 중 2개 고르기 * 그 부위의 개수 ... n개까지
# nC1부터 nCn까지의 합 구하기, 고른 값의 숫자도 곱해야 한다. (고를 때마다 list에 숫자를 넣고 다 골랐을 경우 곱 반환, 다음 고를 때 list는 다시 초기화)
# 재귀? 고른 부위의 숫자 * 1(자기 자신) + 나머지 리스트를 통해 모든 경우에 접근하도록 만들기, 리스트가 한개일 경우 그 숫자 반환
# 리스트에 여러 숫자가 남아있을 경우


# 3 2: 5 + 6
# 3 5 7: 3 + 5 + 7 + 105 +
# 리스트를 입력하면 그 리스트에 속한 모든 원소들의 곱을 반환
# 재귀를 사용하여 리스트 만들기?
# 5종류가 있다면 반복문으로 각 종류의 경우의 수 * 4가지로 가능한 경우의 수 반복
#

import sys
rl = sys.stdin.readline

t = int(rl())

for _ in range(t):
    cloth_list = dict()
    n = int(rl())

    for i in range(n):
        a = rl().split()[1]
        if a not in cloth_list:
            cloth_list[a] = 1
        else:
            cloth_list[a] += 1

    cloth_list = list(cloth_list.values())

    _count = 1
    for i in cloth_list:
        _count *= (i+1)

    print(_count-1)

""" import sys
rl = sys.stdin.readline


def case(L):
    if len(L) == 1:
        return L[0]
    else:
        _sum = mul(L)
        for i in range(len(L)):
            _sum += case(L[:i]+L[i+1:])
        return _sum


def mul(L):
    _mul = 1
    for i in L:
        _mul *= i
    return _mul


t = int(rl())

for _ in range(t):
    cloth_list = dict()
    n = int(rl())

    for i in range(n):
        a = rl().split()[1]
        if a not in cloth_list:
            cloth_list[a] = 1
        else:
            cloth_list[a] += 1

    cloth_list = list(cloth_list.values())

    print(case(cloth_list)) """
