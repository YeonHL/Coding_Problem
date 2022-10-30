a, b, c = map(int, input().split())
d = int(input())

_second = c + d % 60
_minute = b + (d % 3600) // 60
_hour = a + d // 3600
if _second >= 60:
    _minute += 1
    _second %= 60

if _minute >= 60:
    _hour += 1
    _minute %= 60

if _hour >= 24:
    _hour %= 24

print(_hour, _minute, _second)
