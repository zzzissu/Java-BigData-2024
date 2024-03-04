# file : p56_slackmsg.py
# desc : 슬랙으로 스마트폰 메세지 보내기

'''
순서
1. https://api.slack.com/ 에서 your apps > Create your first app
2. From Scratch 클릭    > 앱 이름은 영어로만
3. 워크스페이스 선택
4. Incomming Webhooks > on > Add New Webhook to Workspace 클릭 > 채널선택 > 허용
'''
# https://hooks.slack.com/services/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

import requests
import json

slack_url = 'https://hooks.slack.com/services/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'

headers = {'Content-type': 'application/json'}
data = {'text': 'Python에서 보내는 메세지'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200:
    print('메세지 전송성공')
else:
    print('메세지 전송실패')
