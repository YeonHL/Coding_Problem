def solution(N):
    # write your code in Python 3.6
    N = bin(N)
    count = 0
    m_count = 0
    c = 0
    for i in range(3, len(N)):
        if N[i] == '0':
            count += 1
            if count > m_count:
                m_count = count
        elif N[i] == '1':
            m_count = count
            count = 0
            c = 1

    if c == 0:
        return 0
    else:
        return m_count


n = int(input())
print(solution(n))
