# file : p08_review.py
# desc : 리뷰

print('----------------')
print('*** 2장 리뷰 ***')
print('----------------')

# Q2
print('Q2번:')
# -------------------------
a = 13
print('a는 ', end = '')
if a % 2 == 0:
    print('짝수')
else:
    print('홀수')
# --------------------------
print('----------------')

# Q3
print('Q3번:')
# --------------------------
pin = "88881120-1168234"
yyyymmdd = pin.split('-')[0]    # first = 'yyyymmdd= '
num = pin.split('-')[1]         # sec = 'num = '
print(yyyymmdd)                 # print(frist + pin[0:8])
print(num)                      # print(sec + pin[9:16])
# --------------------------
print('----------------')


# Q5
print('Q5번:')
# --------------------------
a = "a:b:c:d"
b = a.replace(':', '#') # :을 #으로 대체
print(b)
# --------------------------
print('----------------')


# Q6
print('Q6번:')
# --------------------------
a = [1, 3, 5, 4, 2]
a.sort()
a.sort(reverse=True)
print(a)
# --------------------------
print('----------------')


# Q10
print('Q10번:')
# --------------------------
a = {'A':90, 'B':80, 'C': 70}
result = a.pop('B')
print(a)
print(result)
# --------------------------