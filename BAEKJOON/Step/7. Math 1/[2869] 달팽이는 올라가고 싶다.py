import sys

a, b, v = map(int, sys.stdin.readline().rstrip().split())

print((v-b-1) // (a-b)+1)

# v-b-1 지점은 정상 직전에서 b만큼 내려간 위치이다.
# (v-b-1) / (a-b)+1보다 큰 날짜가 지나면 정상에 도착이 가능하므로 몫을 구한 뒤 1을 더해준다.
