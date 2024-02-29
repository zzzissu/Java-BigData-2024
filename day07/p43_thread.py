# file : p43_thread.py
# desc : 스레드 기본
# 하나의 프로세스에 여러개 스레드

from threading import Thread, current_thread
import time

class BackgroundWorker(Thread):
    def __init__(self, name) -> None :
        super().__init__(name = name)
        self._name = f'{current_thread().name()} : {name}'
        # self._name = f'{current_thread().getName()} : {name}'     getname은 업그레이드 버전에서 이제 사용 못함
        
        
    def run(self) -> None:
        print(f'백그라운드 워커 시작 : {self._name}')
        time.sleep(3)
        print(f'백그라운드 워커 종료 : {self._name}')

print('메인 스레드 시작')   # 메인 엔트리에서 시작되는 프로세스 자신(메인스레드)

for i in range(5):
    name = f'서브스레드 {i}'
    th = BackgroundWorker(name)
    th.start()  # run이 실행
    
print('메인 스레드 종료')