# file : p33_osDir.py
# desc : 운영체제 디렉토리 확인

import os   #OS에서 필요한 라이브러리

def search(dirName):
    try:
        fileNames = os.listdir(dirName) # 결과는 list
        for fileName in fileNames:
            fullName = os.path.join(dirName, fileName)  #str타입
            if os.path.isdir(fullName):
                search(fullName)    # 재귀호출
            else:
                ext = os.path.splitext(fullName)[-1]    # tuple의 제일 뒤의 값 str  #ext = 확장자를 조회
                if ext == '.py':    # 파이썬 파일만 출력
                    with open(fullName, mode='r', encoding='utf-8') as fp:      #with로 파일 열면 close() 필요없음
                        print(f'파일명 : {fullName}, 라인수 : {len(fp.readlines())}줄')
    except PermissionError as e:    # 접근권한이 없을 때
        print('접근권한이 없습니다', e.args)
        

if __name__ == '__main__':  # main extry
    search('C:/Source/java-bigdata-2024') # OS 드라이브 경로에서 \는 되도록 쓰지말것
    