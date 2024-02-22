# file : p06_bool.py
# desc : 불(리언)타입, None타입 학습

# 참/거짓

a = True
b = False

print(a)
print(type(a))  # <class 'bool'>
print(type(1))  # <class 'int'>
print(type(3.14)) # <class 'false'>
print(type('Hi'))   # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>

print(a == b)
print(a != b)   # or (a == (not b))

print(bool(0))  # {} 빈 값, 0, None은 false, 그 외는 true

## None 타입

c = None
a = 1
b = 0
print(c)
print(a + b)
print(c + a)    # a true(1) false(0)
