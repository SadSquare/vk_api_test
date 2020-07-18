'''import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random 
from random import randint

def write_msg(user_id, message):
    vk.method('message.send',{'user_id':user_id,'message':message})
    token = "75a28e576079c89b55971015cf685314d4f93f42a8302ab3e774a4307f6bd2bb103b768f2423e8b9b1000"
    
    vk = vk_api.VkApi(token = token)
    longpoll = VkLongPoll(vk)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text

                if request == "roll" or "Roll" or "ROLL" or "/roll":
                    roll = random.randint(0, 100)
                    roll = str(roll)
                    roll = "Roll: " + roll
                    write_msg(event.user_id, roll)
                else:
                    write_msg(event.user_id, "...")
write_msg()
'''
import requests
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import random 
from random import randint

token = "75a28e576079c89b55971015cf685314d4f93f42a8302ab3e774a4307f6bd2bb103b768f2423e8b9b1000"

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:		
        if event.text == 'roll' or event.text == '/roll': 
            if event.from_user:
                roll = random.randint(0, 100)
                roll = str(roll)
                roll = "Roll: " + roll
                

                vk.messages.send(user_id=event.user_id, message=roll, random_id = 0)
            elif event.from_chat:
                vk.messages.send(chat_id = event.chat_id, message = "...")
        else:
            if event.from_user:
                roll = ""
                vk.messages.send(user_id=event.user_id, random_id = 0)
            
        

    