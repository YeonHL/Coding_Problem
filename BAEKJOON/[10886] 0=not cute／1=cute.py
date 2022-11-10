n = int(input())

cnt = 0
for _ in range(n):
    if int(input()) == 1:
        cnt += 1

if cnt < n-cnt:
    print("Junhee is not cute!")
elif cnt > n-cnt:
    print("Junhee is cute!")
