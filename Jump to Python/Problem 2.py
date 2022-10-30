"""
1. 3의 배수의 합

sum = 0
i = 1

while (i <= 1000):
    if i % 3 == 0:
        sum += i
    i += 1
print(sum)
"""

""" 
2. * 출력

i = 1
while (i <= 5):
    print("*"*i, end='')
    print(' ')
    i += 1
"""

""" 
3. 1부터 100 출력

for i in range(1, 101):
    print(i)
"""

"""
4. 평균 점수 구하기

sum = 0

for i in [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]:
    sum += i
print(sum/10)
"""

"""
5. 리스트 내포

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
"""
