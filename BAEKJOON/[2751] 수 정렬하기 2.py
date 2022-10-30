import sys
rl = sys.stdin.readline

n = int(rl())

li = list()

for _ in range(n):
    li.append(int(rl()))

li.sort()
for l in li:
    print(l)


# 아래가 실행 시간은 더 짧다.
# 숫자가 중복되지 않음을 이용, Table을 미리 만들고 숫자를 해당 순서에 입력하여 True로 전환한 뒤
# True를 갖는 숫자만 list에 추가하여 출력한다.

""" import sys
input = sys.stdin.readline

N = int(input())
num = [0]*2000001

for _ in range(N):
    num[int(input())+1000000] = 1

print('\n'.join([str(i-1000000) for i in range(2000001) if num[i]])) """
