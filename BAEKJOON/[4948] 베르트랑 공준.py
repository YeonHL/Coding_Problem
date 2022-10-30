import sys
rl = sys.stdin.readline

while True:
    n = int(rl())

    if n == 0:
        break

    # 1은 False, 이외의 2n까지의 홀수 개수만큼의 Table을 선언했다.
    li = [False] + [True] * ((2*n - 1) // 2)
    for x in range(1, int((2*n)**.5/2+1)):  # 3부터 n의 제곱근까지의 홀수에 접근한다.
        if li[x]:  # 1을 제외한 x번째 홀수가 가 True일 경우
            li[2*x*(x+1)::x*2+1] = [False] * ((((2*n + 1) // 2) -
                                               x * x * 2) // (x * 2 + 1))
            # x*2+1로 홀수의 실제값을 구하고 (홀수 * 홀수보다 큰 숫자)부터 홀수의 배수를 False로 바꾼다. 홀수보다 작은 숫자는 앞에서 계산했을 것이기 때문
    if n+1 <= 2:  # 최소 숫자가 2보다 작을 경우 2를 따로 처리, 이 문제에서는 갯수에 +1
        print(len(list(filter(bool, li[(n+1)//2:])))+1)
    else:
        print(len(list(filter(bool, li[(n+1)//2:]))))
    # n+1 이상의 홀수를 나타낸 Table의 요소 중 True의 수를 반환한다.
