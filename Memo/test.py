from typing import List


def solution(queries: List[List[int]]) -> int:
    answer = 0

    D = dict()
    Number = dict()

    for z in queries:
        i = 1
        try:
            D[z[0]] += z[1]
            if 2 ** Number[z[0]] < D[z[0]]:
                answer += D[z[0]]
                while (2 ** i < z[1]):
                    i += 1
        except KeyError:
            D[z[0]] = z[1]
            while (2 ** i < z[1]):
                i += 1
        Number[z[0]] = i
    return answer
