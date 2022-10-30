import sys

_input = sys.stdin.readline().rstrip()

for i in range(97, 123):
    if chr(i) in _input:
        print(_input.find(chr(i)), end=" ")
    else:
        print(-1, end=" ")
