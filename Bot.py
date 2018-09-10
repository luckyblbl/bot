# -*- coding: utf-8 -*-

import requests
import datetime
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType


def dni(den,nedelya):



    if nedelya % 2 == 0:
        if den == 0:
            den = "Понедельник"
        if den == 1:
            den = "Вторник"
        if den == 2:
            den = "Среда"
        if den == 3:
            den = "Четверг"
        if den == 4:
            den = "1 пара ( Т205, 10:10-11:40):\nОбщ. Физ. Практикум\n\n2 пара (Т308, 11:50-13:20):\nЭл. И магнетизм\n\n3 пара (Т308, 13:40-15:10):\nЭл. И магнетизм\n\n4 пара ( Т205, 15:20-16:50):\nОбщ. Физ. Практикум\n\nВезде Михайлов"
        if den == 5:
            den = "Суббота"
        if den == 6:
            den = "Воскресенье"
    else:
        if den == 0:
            den = "Понедельник"
        if den == 1:
            den = "Вторник"
        if den == 2:
            den = "Среда"
        if den == 3:
            den = "Четверг"
        if den == 4:
            den = "Пятница"
        if den == 5:
            den = "Суббота"
        if den == 6:
            den = "Воскресенье"
    return den

def main():
    session = requests.Session()


    vk_session = vk_api.VkApi(token='0169b8351a0575b208a63c327a49c20a70b923c90e9a609ad28e3f16d96322b6aaa9d17a1603e25a891fd')


    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')

            response = session.get(
                'http://api.duckduckgo.com/',
                params={
                    'q': event.text,
                    'format': 'json'
                }
            ).json()









            chetv="Ин-яз \n ЧИСЛ.МЕТОДЫ \n ТФКП \n ТФКП"
            pyatnica="ОБЩ.ФИЗ.ПРАКТ. \n ЭЛЕКТР. И МАГНЕТИЗМ	\n ЭЛЕКТР. И МАГНЕТИЗМ	\n ОБЩ.ФИЗ.ПРАКТ."

            nedelya=datetime.date.today().isocalendar()[1]
            den = datetime.date.today().weekday()

            attachments=[]
            #text='Женя {txt}'.format(txt=event.text)
            if event.text.lower()=="пары":
                text = dni(den,nedelya)
            elif event.text.lower() == "пары завтра":
                text=dni(den+1,nedelya)
            elif event.text.lower() == "help":
                text="Все команды --------"
            else:
                text="Введите команду"
            vk.messages.send(
                user_id=event.user_id,
                attachment=','.join(attachments),
                message=text
            )
            print('ok')


if __name__ == '__main__':
    main()