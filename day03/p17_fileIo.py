# file : p17_fileIo.py
# desc : 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 할 것들
# 1. 파일 open(), close() / (파이썬은 크게 상관 없음)
# 2. network open(), close()
# 3. DB open()(or connect), close()

# 언어체계 추가 ASCII(한글 CodePage949), 유니코드(utf-8)
# 상대경로, 절대경로
# .(본인 파일), ..(부모 파일)
f = open('./day03/sample.txt',mode = 'w', encoding = 'utf-8')
# open('./samlpe.txt', 모드)
# ./ = 어디 내부의~
# encoding = 언어체계 설정
# r = 읽기모드: 텍스트 파일에서 글을 읽어오는 것
# w = 쓰기모드: 파일 내용을 쓸때 사용
# a = 추가모드: 어팬드(기존 파일에 글을 추가시키는 것) = 로그 등을 남길 때 사용

# 파일 쓰기 진행
f.write('안녕하세요 파이썬\n')  # 한줄 내려서 출력 하려면 \n 사용
f.write('모두 화이팅')
f.close()   # 파이썬에서는 옵션  # 다른 언어에서는 close를 안하면 다른 곳에서 접근 불가능

