import requests
from bs4 import BeautifulSoup
import schedule
import time

origin = 580
url = 'https://www.panda-novel.com/details/shadow-slave(YN)-1413'
div = origin
def task():
    global div
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('i', class_='iconfont icon-chapter').find_next().text
    return div

print(task())

schedule.every(2).minutes.do(task)

while True:
    if int(div) != origin:
        print('Вышла новая глава :', div)
        print('#' * 20)
        break
    schedule.run_pending()
    time.sleep(30)