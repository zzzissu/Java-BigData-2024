# file : p18_fileRead.py
# desc : 텍스트 파일 읽기

f = open('./day03/sample', mode='r', encoding='utf-8')
f2 = open('./day03/dest.txt', mode='w', encoding='utf-8')
###
read = f.readlines()        # readline으로 하면 한 줄만 읽어옴 > s를 붙혀 주면 모두 가져옴
print('파일에서 읽은 내용 > ', read)
for line in read:
    print(line.replace('\n',''))     
    # (line)만 입력하면 \n부분까지 포함되어 2줄이 띄어짐.
    # 때문에 replace('\n')으로 \n부분을 삭제 시켜주면 원하는데로 출력할 수 있음
    f2.write(line)  # 텍스트 파일 copy하기
    
f.close()
f2.close()