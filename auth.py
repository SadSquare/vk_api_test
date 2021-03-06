# -*- coding: utf-8 -*-
import vk_api


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main():
    """ Пример обработки двухфакторной аутентификации """

    login, password = '89996015169', 'crafter25840'
    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )
    vk_session.auth()
    vk = vk_session.get_api()
    vk.messages.send(user_id = 148545742, random_id = 0,message = "Тестирую бота не обращай внимания")
    try:
        vk_session.auth()
        
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return


    # ...


if __name__ == '__main__':
    main()
