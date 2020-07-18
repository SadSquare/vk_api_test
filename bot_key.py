import requests
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardButton, VkKeyboardColor
from vk_api.utils import get_random_id
import random 
from random import randint


token = "dc519ae7b139d94a596397c874a60a1968f90f8bf190c2fcd342a9e766d8155914d0660c945b197fb7636"

def main():
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_location_button()
    
    keyboard.add_line()
    keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=74030368&aid=6222115")
    
    keyboard.add_line()
    keyboard.add_vkapps_button(app_id=6979558, 
                               owner_id=-181471269, 
                               label="Отправить клавиатуру",
                               hash="sendKeyboard")
                               

    vk.messages.send(peer_id=123456, random_id=0, keyboard=keyboard.get_keyboard(), message='Пример клавиатуры')


if __name__ == '__main__':
    main()
