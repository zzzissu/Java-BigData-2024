# file : p57_mailReceive.py
# desc : 메일 수신

import imaplib
import email
from email import policy

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'gkswltn1223'
pwd = 'hans0807@'
res = imap.login(id, pwd)

if res[0] == 'OK':
    imap.select('INBOX')
    resp, data = imap.uid('search', None, 'All')
    allEmails = data[0].split()
    lastEmails = allEmails[-5:]

    print(lastEmails)
    
    for mail in lastEmails:
        result, data = imap.uid('fetch', mail, '(RFC822)')  # RFC822 메세지 표준형식
        rawEmail = data [0][1]
        emailMessage = email.message_from_bytes(rawEmail, policy=policy.default)

        print('=' * 80)
        print(f'보내시는 분 : {emailMessage['From']}')
        print(f'받으시는 분 : {emailMessage['To']}')
        print(f'수 신 일 자 : {emailMessage['Date']}')
        subject, encode = find_encoding_info(emailMessage['Subject'])
        print(f'제       목 : ')
        
        print('내      용 : ')
        msg = ''
        if emailMessage.is_multipart(): # 첨부파일까지 포함된 메일인가
            for part in emailMessage.get_payload():
                if part.get_content_type() == 'text/plain':
                    bytes = part.get_payload(decode=True)
                    encode = part.get_content_charset()
                    msg = msg + str(bytes, encode)  # 인코딩을 자신의 언어에 맞춰서  변경
        else:   # multipart 형식이 아닌경우
            part = emailMessage.get_payload()
            print(part)
            
            
        print(msg)


    imap.close()
    imap.logout()   # 파이썬이 아닌 다른 언어에서는 close()나 logout()이 필수..