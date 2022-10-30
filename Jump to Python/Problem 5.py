# 1. 문자열 바꾸기

""" s = "a:b:c:d"
l = s.split(":")
a = ""

for i in l:
    a += i

s = "#".join(a) """

# 2. Dictionary 값 추출

""" a = {'A': 90, 'B': 80}

try:
    print(a['C'])
except KeyError:
    print(70) """

# 3. List 총합 구하기 (한줄로 만들 수 있지 않을까?)

""" A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0

for i in A:
    if i >= 50:
        sum += i

print(sum) """

# 4. 피보나치 함수

""" l = [1, 1]
i = 1
n = int(input("숫자를 입력하시오."))

while (l[i-1] + l[i] <= n):
    l.append(l[i-1]+l[i])
    i += 1

print(l) """

# 5. 숫자의 총합 구하기

""" s = input("숫자를 입력하시오 (,로 구분)")
l = s.split(",")
sum = 0

for i in l:
    sum += int(i)

print(sum) """

# 6. 한 줄 구구단

""" i = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))

while not 2 <= i <= 9:
    i = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))


for x in range(1, 10):
    print(i*x, end=" ") """


# 7. 역순 저장

""" f = open("text.txt", 'w')
f.write("AAA\nBBB\nCCC\nDDD\nEEE\n")
f.close() """

""" f = open("text.txt", 'r')
a = f.readlines()
a.reverse()
f.close()

f = open("text.txt", 'w')
for line in a:
    f.write(line)
f.close()

print(f)
"""

# 8. 평균값 구하기

""" f = open("text.txt", 'w')
f.write("70\n60\n55\n75\n95\n90\n80\n80\n85\n100")
f.close()

f = open("text.txt", 'r')
a = f.readlines()
f.close()

sum = 0

for i in a:
    sum += int(i)

avg = sum / 10

f = open("result.txt", 'w')
f.write("sum: " + str(sum) + " \navg: " + str(avg)) """


# 9. 사칙연산 계산기

""" class Calculator:
    def __init__(self, l):
        self.ls = l

    def sum(self):
        return sum(self.ls)

    def avg(self):
        return sum(self.ls) / len(self.ls)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg()) """

# 10. DashInsert 함수


""" def DashInsert(s):
    a = ",".join(s)
    l = a.split(',')
    result = "" + str(l[0])

    for i in range(1, len(l)):
        if (int(l[i-1]) % 2 == 0) & (int(l[i]) % 2 == 0):
            result = result + "*" + str(l[i])
        elif (int(l[i-1]) % 2 == 1) & (int(l[i]) % 2 == 1):
            result = result + "-" + str(l[i])
        else:
            result += str(l[i])

    print(result)


DashInsert('45467935467457') """


# 11. 문자열 압축하기

""" def compress(s):
    result = ""
    count = 1

    n = 1
    while (n < len(s)):
        while (s[n-1] == s[n]):
            count += 1
            if n+1 == len(s):
                break
            else:
                n += 1
        if n+1 == len(s):
            if s[n-1] != s[n]:
                result = result + s[n-1] + str(count) + s[n] + '1'
                break
            else:
                result = result + s[n-1] + str(count)
                break
        result = result + s[n-1] + str(count)
        count = 1
        n += 1

    print(result)

compress("aaabbcccccca") """

# 12. Duplicate Numbers

""" a = input("숫자를 입력하시오 (공백으로 구분): ")
b = a.split()

for i in b:
    for j in range(10):
        if i.count(str(j)) > 1:
            print("False", end=" ")
            break
        elif j == 9:
            print("True", end=" ") """


# 13. 모스 부호 해독


""" a = input("모스 부호를 입력하시오 (공백으로 구분, 공백 2개는 단어 사이) ")
b = a.split("  ")


for s in b:
    c = s.split()
    for t in c:
        if t == '.-':
            print('A', end='')
        elif t == '-...':
            print('B', end='')
        elif t == '-.-.':
            print('C', end='')
        elif t == '-..':
            print('D', end='')
        elif t == '.':
            print('E', end='')
        elif t == '..-.':
            print('F', end='')
        elif t == '--.':
            print('G', end='')
        elif t == '....':
            print('H', end='')
        elif t == '..':
            print('I', end='')
        elif t == '.---':
            print('J', end='')
        elif t == '-.-':
            print('K', end='')
        elif t == '.-..':
            print('L', end='')
        elif t == '--':
            print('M', end='')
        elif t == '-.':
            print('N', end='')
        elif t == '---':
            print('O', end='')
        elif t == '.--.':
            print('P', end='')
        elif t == '--.-':
            print('Q', end='')
        elif t == '.-.':
            print('R', end='')
        elif t == '...':
            print('S', end='')
        elif t == '-':
            print('T', end='')
        elif t == '..-':
            print('U', end='')
        elif t == '...-':
            print('V', end='')
        elif t == '.--':
            print('W', end='')
        elif t == '-..-':
            print('X', end='')
        elif t == '-.--':
            print('Y', end='')
        elif t == '--..':
            print('Z', end='')
    print(end = " ") """


# 14. 그루핑


import re
p = re.compile(r"\w+\s+\d+[-]\d+[-](\d+)")
m = p.search("park 010-9999-9988")
(m.group(1))

# 15. 전방 탐색
