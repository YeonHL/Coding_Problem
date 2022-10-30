import sys

n = int(sys.stdin.readline().rstrip())
""" i = 1
num = 0


while (True):
    num += i
    if num >= n:
        if i % 2 == 1:
            nu = 1
            de = i
            while (num != n):
                nu += 1
                de -= 1
                num -= 1
            break
        else:
            nu = i
            de = 1
            while (num != n):
                de += 1
                nu -= 1
                num -= 1
            break
    i += 1

print("{0}/{1}".format(nu, de)) """

# 합이 2,3,4,5로 증가한다. (a+1)
# 짝수 번째의 경우 분자가 1씩 커지고 분모가 1씩 작아진다.
# 홀수 번째의 경우 분자가 1씩 작아지고 분모가 1씩 커진다.
# 마지막 번호는 1부터 a까지의 합이다.

# (1) 1씩 증가시키면서 더해서 n이 합보다 작아지는 i를 찾는다.
# (2) 합에서 1씩 감소시키면서 n과 같아지는 경우와 그 분수를 찾는다.

# 가장 효율적인 풀이

a = 0

while n > 0:
    a += 1
    n -= a

print("%d/%d" % (1-n, a+n)[::a % 2*2-1])  # 뒤의 인덱싱은 a의 홀짝 여부에 따라 불러오는 순서를 바꾼다.
