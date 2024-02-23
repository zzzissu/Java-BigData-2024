# file : p21_review.py
# desc : 리뷰

# Q7
## readlines() 썻을때
f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.readlines()
f.close()

body = [body[0], body[1].replace('java', 'python')]
# print(body)
f. open('./day03/text.txt', mode='w', encoding='utf-8')
f.write(body[0] + body[1])
f.close()

## read() 썻을때
f. open('./day03/text.txt', mode='w', encoding='utf-8')
body = f.read()     # 문자열이기 때문에
f.close()

body = body.replace('java', 'python')
# print(body)
f = open('./day03/text.txt', mode='w', encoding='utf-8')
f.write(body)
f.close()