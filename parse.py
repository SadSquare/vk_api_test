import requests
from bs4 import BeautifulSoup
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime, date, time
import time

def parser(id_obj):
    url = 'https://a55.agorov.org/'
    headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find(id = id_obj).text
    return result

def message_vk(mes):
    token = "20df76bd47c10e08c770927485ec32df51c7d8833a9df961151e59e910abfce2dc3a277c063f19e8f2b1a"
    vk_session = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    vk.messages.send(user_id=307049558, message=mes, random_id = 0)

def if_time(day, ras_day):
    if datetime.today().strftime("%A") == day:
        rasp = parser(ras_day)
        return rasp
    else:
        pass

day_list = {'Sunday':'raspisSun',
            'Monday':'raspisMon',
            'Tuesday':'raspisTue',
            'Wednesday':'raspisWed',
            'Thurday':'raspisThu',
            'Friday':'raspisFri',
            'Saturday':'raspisSat'}
def main():
    while True:
        for day, day_rasp in day_list.items():
            mess = if_time(day,day_rasp)
            try:
                message_vk(mess)
                time.sleep(86400)
            except:
                return main()
if __name__ == "__main__":
    main()
