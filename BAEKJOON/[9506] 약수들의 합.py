# 약수와 나머지 쌍을 추가
# 제곱근보다 작을 때까지만 확인

while True:
    n = int(input())

    if n == -1:
        break

    _list = [1]
    _sum = 1

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            _list.append(n//i)
            _list.append(i)
            _sum += n//i + i
    if _sum == n:
        _list.sort()
        _list = list(map(str, _list))
        print(n, "=", " + ".join(_list))
    else:
        print(n, "is NOT perfect.")
