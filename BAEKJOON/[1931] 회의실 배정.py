# 시간을 시작과 종료 시간으로 리스트에 저장
# 종료 시간을 기준으로 정렬, 같은 값들은 시작 시간 기준으로 정렬
# 종료 시간을 기준으로 비교, 만약 종료 시간이 더 이전인 회의가 있으면 그 종료 시간을 저장, 카운트 + 1


N = int(input())

time = sorted([tuple(map(int, input().split()))
              for _ in range(N)], key=lambda x: (x[1], x[0]))

cnt = 1
f = time[0][1]
for i in range(1, N):
    if time[i][0] >= f:
        cnt += 1
        f = time[i][1]

print(cnt)
