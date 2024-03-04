# file : p57_mailReceive.py
# desc : 메일 수신

import imaplib
import email
from email import policy
import requests
import json

slack_url = 'https://hooks.slack.com/services/T**/B**/0**'
def sendToSlack(msg):
    header = {'content-type': 'application/json'}
    data = {'text': msg}
    res = requests.post(slack_url, headers=header, data=json.dumps(data))
    if res.status_code == 200: return 'OK'
    else: return 'ERROR'

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = '<your id>'
pwd = '<your password>'
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
        
        emailFrom = str(emailMessage['From'])
        emailDate = str(emailMessage['Date'])
        subject, encode = find_encoding_info(emailMessage['Subject'])
        subject = str(subject)
        if subject.find('중요') >= 0:
            slackMessage = f'{emailFrom}\n{emailDate}\n{subject}'
            ret = sendToSlack(slackMessage)
            if ret == 'OK':
                print(f'{subject} 메일 슬랙전송 성공')
            else:
                print(f'{subject} 메일 슬랙전송 실패')
        else:
            print('보낼메세지 없음')


        # print('=' * 80)
        # print(f'보내시는 분 : {emailMessage['From']}')
        # print(f'받으시는 분 : {emailMessage['To']}')
        # print(f'수 신 일 자 : {emailMessage['Date']}')
        # subject, encode = find_encoding_info(emailMessage['Subject'])
        # print(f'제       목 : ')
        
        # print('내       용 : ')
        # msg = ''
        # if emailMessage.is_multipart(): # 첨부파일까지 포함된 메일인가
        #     for part in emailMessage.get_payload():
        #         if part.get_content_type() in ['text/plain', 'text/html']:
        #             bytes = part.get_payload(decode=True)
        #             encode = part.get_content_charset()
        #             msg = msg + str(bytes, encode)  # 인코딩을 자신의 언어에 맞춰서  변경
        # else:   # multipart 형식이 아닌경우
        #     msg = emailMessage.get_payload()
        #     print(msg)

            
        print(msg)


    imap.close()
    imap.logout()   # 파이썬이 아닌 다른 언어에서는 close()나 logout()이 필수..