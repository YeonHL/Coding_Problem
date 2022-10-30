# 평균값에서 올림처리 하므로 평균에서 -1한 후 최종 값에서 1을 더해주면 된다.


a, i = map(int, input().split())
print(a*(i-1)+1)
