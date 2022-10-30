# 1. 클래스 상속

"""
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
"""

# 2. method overriding


""" class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value + val > 100:
            self.value = 100
        else:
            self.value += val """

# 3. filter & lambda

""" a = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x: x > 0, a))) """

# 4. map & lambda

""" l = [1, 2, 3, 4]

list(map(lambda x: x*3, l)) """

# 5. Max & Min

""" a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(min(a) + max(a)) """

# 6. Round

""" print(round(17/3, 4)) """

# 7. sys.argv

""" import sys
i = 0
s = ""

for a in sys.argv:
    if type(a) == str:
        s += a
    elif type(a) == int:
        i += a

print(i)
print(s) """

# 8. os

""" import os
os.chdir("C:/doit")
a = dir()
print(a) """

# 9. glob


""" import glob
glob.glob("C:/doit/*.py") """

# 10. time

""" import time
print(time.strftime('%Y/%m/%d %X', time.localtime(time.time()))) """

# 11. random

""" import random
s = set()
while (len(s) < 5):
    s.add(random.randint(1, 45)) """
