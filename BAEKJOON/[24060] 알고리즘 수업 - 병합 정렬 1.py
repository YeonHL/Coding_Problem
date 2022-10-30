import sys
rl = sys.stdin.readline

n, k = map(int, rl().split())
a = list(map(int, rl().split()))

save_list = []


def merge_sort(A, p, r):
    if (p < r):
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    i = p
    j = q+1
    t = 0
    tmp = [0] * (r-p+1)

    while (i <= q and j <= r):
        if (A[i] <= A[j]):
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1

    while (i <= q):
        tmp[t] = A[i]
        t += 1
        i += 1

    while (j <= r):
        tmp[t] = A[j]
        t += 1
        j += 1

    i = p
    t = 0

    while (i <= r):
        A[i] = tmp[t]
        save_list.append(tmp[t])
        i += 1
        t += 1


merge_sort(a, 0, n-1)
if len(save_list) < k:
    print(-1)
else:
    print(save_list[k-1])
