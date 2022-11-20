# A,B,C,D,E,F,G,H 중 해당하는지 확인한다.
# 모두 해당하지 않을 경우 모든 자리 수를 A~H의 각 자리수와 비교하면서 차이가 1개만 존재하는지 확인한다.
# 모든 알파벳과 2개 이상의 숫자가 다를 경우 그 위치를 반환한다. (1부터 시작)

def check(word):
    crypto = {'000000': 'A', '001111': 'B', '010011': 'C', '011100': 'D',
              '100110': 'E', '101001': 'F', '110101': 'G', '111010': 'H'}

    for x in crypto:
        if word == x:
            return crypto[x]

    for alpha in crypto:
        cnt = 0
        j = 0

        for x in alpha:
            if x != word[j]:
                cnt += 1
            j += 1

        if cnt == 1:
            return crypto[alpha]

    return ''


n = int(input())
message = input()
result = []

for i in range(n):
    c = check(message[i*6:i*6+6])

    if c == '':
        print(i+1)
        break

    result.append(c)

if len(result) == n:
    print(''.join(result))
