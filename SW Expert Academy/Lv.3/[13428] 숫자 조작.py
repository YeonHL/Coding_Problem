# 맨앞 0 고려하기
# 위치는 1번까지만 교환 가능
# 최소값, 최대값 순서 출력
# 해당 숫자로 만들 수 있는 최대값 최소값 구하기
# 이후 현재 값과 최대값, 최소값의 각 자리 수를 비교하면서 다를 경우 그 숫자를 한번 교환
# 최소값의 경우 정렬 후 0이 아닌 값이 나올 때까지 index +1
# 슬라이싱을 활용하여 [i] + [:i] + [i:]
""" from itertools import combinations """

T = int(input())

for test_case in range(1, T + 1):
    M = input()
    _max = ''.join(sorted(M, reverse=1))
    _min = '0'

    temp = sorted(M)

    for i in range(len(temp)):
        if temp[i] != '0':
            if i == len(temp)-1:
                _min = temp[i] + ''.join(temp[:i])
                break
            elif i == 0:
                _min = ''.join(temp)
                break
            _min = temp[i] + ''.join(temp[:i]) + ''.join(temp[i+1:])
            break

    result_max = _max
    result_min = _min

    for i in range(len(M)):
        if M[i] != _max[i]:
            num = 0

            for j in range(len(M)-1, -1, -1):
                if M[j] == _max[i]:
                    num = j
                    break

            if i > num:
                if i == len(M)-1:
                    result_max = M[:num] + M[i] + M[num+1:i] + M[num]
                    break
                result_max = M[:num] + M[i] + M[num+1:i] + M[num] + M[i+1:]
                break
            elif i < num:
                if num == len(M)-1:
                    result_max = M[:i] + M[num] + M[i+1:num] + M[i]
                    break
                result_max = M[:i] + M[num] + M[i+1:num] + M[i] + M[num+1:]
                break

    for i in range(len(M)):
        if M[i] != _min[i]:
            num = 0

            for j in range(len(M)-1, -1, -1):
                if M[j] == _min[i]:
                    num = j
                    break

            if i > num:
                if i == len(M)-1:
                    result_min = M[:num] + M[i] + M[num+1:i] + M[num]
                    break
                result_min = M[:num] + M[i] + M[num+1:i] + M[num] + M[i+1:]
                break
            elif i < num:
                if num == len(M)-1:
                    result_min = M[:i] + M[num] + M[i+1:num] + M[i]
                    break
                result_min = M[:i] + M[num] + M[i+1:num] + M[i] + M[num+1:]
                break

    print(f"#{test_case} {result_min} {result_max}")


""" data = list(map(str, input()))
    target = [i for i in range(len(data))]

    min_value, max_value = int(''.join(data)), int(''.join(data))

    for value in combinations(target, 2):
        i, j = value
        data[i], data[j] = data[j], data[i]
        if data[0] == '0':
            data[i], data[j] = data[j], data[i]
            continue
        if int(''.join(data)) < min_value:
            min_value = int(''.join(data))
        if int(''.join(data)) > max_value:
            max_value = int(''.join(data))
        data[i], data[j] = data[j], data[i]

    print('#%d %d %d' % (test_case, min_value, max_value)) """
