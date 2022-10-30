import sys
rl = sys.stdin.readline

n = int(rl())
queue = [0]*2000000
front = rear = 0

for _ in range(n):
    a = rl().split()

    if a[0] == "push":
        queue[rear] = a[1]
        rear += 1
    elif a[0] == "pop":
        if front == rear:
            print(-1)
        else:
            print(queue[front])
            front += 1
    elif a[0] == "size":
        print(rear - front)
    elif a[0] == "empty":
        if front == rear:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if front == rear:
            print(-1)
        else:
            print(queue[front])
    elif a[0] == "back":
        if front == rear:
            print(-1)
        else:
            print(queue[rear-1])

# pop이나 Indexing, Remove의 경우 시간이 초과된다. 삭제 대신 다른 방법을 사용해야 한다.
# 예시

""" import sys

def solve():
    q = [0]*2000000
    front = rear = 0
    res = []
    for string in sys.stdin.read().splitlines()[1:]:
        t = string[1]
        if t == "u":
            q[rear] = string[5:]
            rear += 1
        elif t == "o":
            if front == rear:
                res.append('-1')
            else:
                res.append(q[front])
                front += 1
        elif t == "i":
            res.append(str(rear-front))
        elif t == "m":
            res.append('1' if front == rear else '0')
        elif t == "r":
            res.append(q[front] if front != rear else '-1')
        elif t == "a":
            res.append(q[rear-1] if front != rear else '-1')

    sys.stdout.write('\n'.join(res))


if __name__ == '__main__':
    solve() """
