# file : p32_review.py
# desc : 리뷰

print('----------------')
print('*** 5장 리뷰 ***')
print('----------------')

# Q1
print('Q1번:')
# --------------------------
class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -=val
        
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
# --------------------------
print('----------------')


# Q2
print('Q2번:')
# --------------------------
class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.vlaue = 100
            
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
# --------------------------
print('----------------')


# Q6
print('Q6번:')
# --------------------------
print(list(map(lambda x:x*3, [1, 2, 3, 4])))
# --------------------------
print('----------------')


# Q7
print('Q7번:')
# --------------------------
a = [-8, 2, 7, 5, -3, 5, 0, 1]
b = max(a) + min(a)
print(b)
# --------------------------
print('----------------')


# Q11
print('Q11번:')
# --------------------------
import time
print(time.strftime('%Y/%m/%d %H:%M:%S'))
# --------------------------
print('----------------')