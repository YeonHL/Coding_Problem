""" import sys
rl = sys.stdin.readline

m, n = map(int, rl().split())

pt = [False] + [True for t in range(n-1)]

i = 2

while i*i <= n:
    if pt[i-1]:
        for x in range(i*2-1, n, i):
            pt[x] = False

    i += 2 if i > 2 else 1

for x in range(m-1, n):
    if pt[x]:
        print(x+1) """

# 처음 성공한 코드


m, n = map(int, input().split())
# 1은 False, 이외의 n까지의 홀수 개수만큼의 Table을 선언했다.
li = [False] + [True] * ((n - 1) // 2)
for x in range(1, int(n**.5/2+1)):  # 3부터 n의 제곱근까지의 홀수에 접근한다.
    if li[x]:  # 1을 제외한 x번째 홀수가 가 True일 경우
        li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) -
                                           x * x * 2) // (x * 2 + 1))
        # x*2+1로 홀수의 실제값을 구하고 (홀수 * 홀수보다 큰 숫자)부터 홀수의 배수를 False로 바꾼다. 홀수보다 작은 숫자는 앞에서 계산했을 것이기 때문
if m <= 2:
    print(2)  # 최소 숫자가 2보다 작을 경우 2를 따로 처리, 이 문제는 소수의 출력이므로 2를 출력했다.
print('\n'.join([f'{x}' for x, val in zip(
    range(m+(m & 1 == 0), n+1, 2), li[m//2:]) if val]))
# 비트 연산자 & 사용, m이 짝수일 경우 소수가 아니므로 시작값에 1을 더해준다.
# m부터 n까지의 홀수 리스트와 m 이상의 홀수 중 소수를 나타낸 Table의 각 요소를 Tuple로 묶고 그 중 Table의 값이 True인 x만 리스트로 반환하고, 그 리스트의 각 요소를 \n로 구분하여 출력한다.
