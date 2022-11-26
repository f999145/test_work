import requests
from bs4 import BeautifulSoup
import schedule
import time

origin = 574
url = 'https://www.panda-novel.com/details/shadow-slave(YN)-1413'

div = origin
def task():
    global div
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('i', class_='iconfont icon-chapter').find_next().text
    return

schedule.every(1).minutes.do(task)

while True:
    if int(div) != origin:
        print('Новая глава :', div)
        break
    schedule.run_pending()
    time.sleep(1)
    