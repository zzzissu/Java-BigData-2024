# file : p14_review.py
# desc : 리뷰

print('----------------')
print('*** 3장 리뷰 ***')
print('----------------')

## Q1
print('Q1번:')
# --------------------------
a = 'Life is too short, you need puthon'

if "wife" in a: print("wife")
elif "python"in a and " you" not in a: print("python")
elif " shirt" not in a: print("shirt")
elif " need" in a: print("need")
else: print("none")
# --------------------------
print('----------------')

## Q2
print('Q2번:')
# --------------------------
result = 0
i = 1

while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
    
print(result)
# --------------------------
print('----------------')

## Q3
print('Q3번:')
# --------------------------
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * 1)
# --------------------------
print('----------------')

## Q4
print('Q4번:')
# --------------------------
for i in range(1, 101):
    print(i)
# --------------------------
print('----------------')

## Q5
print('Q5번:')
# --------------------------
A = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)
# --------------------------
print('----------------')

## Q6
print('Q6번:')
# --------------------------
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)

result = [n * 2 for n in numbers if n % 2 == 1]
print(result)