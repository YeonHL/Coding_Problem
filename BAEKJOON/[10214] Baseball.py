T = int(input())

for _ in range(T):
    Yonsei = 0
    Korea = 0

    for _ in range(9):
        Y, K = map(int, input().split())
        Yonsei += Y
        Korea += K

    if Yonsei > Korea:
        print("Yonsei")
    elif Yonsei < Korea:
        print("Korea")
    elif Yonsei == Korea:
        print("Draw")
