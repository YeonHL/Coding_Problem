import sys
rl = sys.stdin.readline

t = int(rl())

for i in range(t):
    k = int(rl())
    n = int(rl())

    apart = list(range(1, n+1))

    for a in range(k):
        for b in range(1, n):
            apart[b] += apart[b-1]

    print(apart[-1])


# 0층부터 있고 각 층에도 1호부터 있으며 0층의 i호에는 i명이 산다.
# k층의 n호에 살고 있는 인원의 수, k-1층의 1~n호까지 사람들의 수의 합이다.
# 규칙성은 아래층 + 앞 호실의 수이다. 리스트를 Memory처럼 사용하여 이전 층의 사람의 수를 저장한다.
