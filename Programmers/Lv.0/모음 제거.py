def solution(my_string):
    answer = ''
    _check = 'aeiou'

    for i in my_string:
        if i in _check:
            continue
        answer += i

    return answer
