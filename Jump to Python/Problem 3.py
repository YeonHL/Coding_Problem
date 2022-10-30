"""
1. 홀짝 구분 함수

def is_odd(i):
    print("홀수") if i % 2 == 1 else print("짝수")
"""

"""
2. 평균 값 계산

def average(*number):
    sum = 0
    for i in number:
        sum += i
    return sum / len(number)
"""

"""
3. 입력 값 반환

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
"""

"""
4. 문자열 추가 & 출력
f1 = open("test.txt", 'a')
f1.write("Life is too short\n")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
"""


# 5. 문자열 변환 후 저장

f1 = open("test.txt", 'w')
f1.write("Life is too short\n")
f1.write("you need java\n")
f1.close()

with open("test.txt", 'r+') as file:
    data = file.read()

with open("test.txt", "w+") as file:
    data = data.replace("java", "python")
    file.write(data)
