def solution(today, terms, privacies):
    answer = []
    x = 1
    for p in privacies:
        a, b = p.split()
        c, d, e = a.split('.')
        for t in terms:
            f, g = t.split()
            if b == f:
                break
        d = int(d) + int(g)
        if d % 12 == 0:
            c = int(c) + (d // 12 - 1)
            d = 12
        else:
            c = int(c) + d // 12
            d = d % 12

        h, i, j = today.split('.')

        if int(h) > c:
            answer.append(x)
        elif int(h) < c:
            pass
        else:
            if int(i) > d:
                answer.append(x)
            elif int(i) < d:
                pass
            else:
                if int(j) >= int(e):
                    answer.append(x)
                else:
                    pass
        x += 1
    return answer
