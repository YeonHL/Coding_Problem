""" import sys
rl = sys.stdin.readline

def binary_search(_list, _target, _start, _end):
    if _start > _end:
        return 0
    mid = (_start + _end) // 2

    if _list[mid] == _target:
        return 1
    elif _list[mid] > _target:
        return binary_search(_list, _target, _start, mid-1)
    else:
        return binary_search(_list, _target, mid+1, _end)


n = int(rl())
n_list = list(map(int, rl().split()))
n_list.sort()

m = int(rl())
m_list = list(map(int, rl().split()))

for i in m_list:
    print(binary_search(n_list, i, 0, n-1))
 """

import sys
rl = sys.stdin.readline

n = int(rl())
n_set = set(map(int, rl().split()))

m = int(rl())
m_list = list(map(int, rl().split()))

for i in m_list:
    if i in n_set:
        print(1)
    else:
        print(0)


# m_list의 숫자가 n_list 내에 존재하는가? 존재하면 1, 아닐 경우 0
