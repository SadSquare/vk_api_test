import requests
from bs4 import BeautifulSoup
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime, date, time
import time

def parser(id_obj):
    url = 'https://a55.agorov.org/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find(id = id_obj).text
    return result

def ran_func_int(rand_range_x, rand_range_y):
    random_num = str(random.randint(rand_range_x, rand_range_y))
    return random_num

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

'''     
while True:
    if datetime.today().strftime("%A") == 'Sunday':
        rasp = parser('raspisSun')
        message_vk(rasp)
    if datetime.today().strftime("%A") == 'Monday':
        rasp = parser('raspisMon')
        message_vk(rasp)
        
    if datetime.today().strftime("%A") == 'Tuesday':
        rasp = parser('raspisTue')
        message_vk(rasp)
        
    if datetime.today().strftime("%A") == 'Wednesday':
        rasp = parser('raspisWed')
        message_vk(rasp)
        
    if datetime.today().strftime("%A") == 'Thursday':
        rasp = parser('raspisThu')
        message_vk(rasp)
        
    if datetime.today().strftime("%A") == 'Friday':
        rasp = parser('raspisFri')
        message_vk(rasp)
    if datetime.today().strftime("%A") == 'Saturday':
        rasp = parser('raspisSat')
        message_vk(rasp)
    else:
        message_vk("Бот поломался") 
        break
    time.sleep(86400)'''
