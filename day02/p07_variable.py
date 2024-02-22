# file : 07_variable.py
# desc : 변수에 대하여
from copy import copy
a = [1, 2, 3]
print(id(a))
b = a       # 주소값이 같음
print(id(b))

# del b[2]
# print(a)

d = copy(a)     # 값을 분리 시킬 때 copy 사용
print(id(d))
del d[2]
print(a)
