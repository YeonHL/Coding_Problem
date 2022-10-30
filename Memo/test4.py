def solution(numbers):
    answer = []
    for n in numbers:
        a = bin(n)
        a = a[2:len(a)]
        for i in range(len(a)):
            if i == len(a)-1:
                if i % 2 == 0:
                    answer.append(1)
                    break
                else:
                    if a[i] == "0" and a[i-1] == "1":
                        answer.append(0)
                        break
                    else:
                        answer.append(1)
                        break
            if i % 2 == 1:
                if a[i] == "0":
                    if a[i-1] == "1" or a[i+1] == "1":
                        answer.append(0)
                        break
    return answer


print(solution([465464, 6546, 14, 86, 6, 6, 46, 841, 684, 31, 4, 4, 416]))
