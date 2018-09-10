# -*- coding: utf-8 -*-
# скрипт был создан автором канала IT THINGS:https://www.youtube.com/c/ITTHINGS

import vk_api
import time
import datetime
import json

vk = vk_api.VkApi(token="0169b8351a0575b208a63c327a49c20a70b923c90e9a609ad28e3f16d96322b6aaa9d17a1603e25a891fd")
vk._auth_token()


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
        if den==7:
            den=None
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
        if den==7:
            den=None
    return den

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": False,
    "buttons": [

    [get_button(label="Пары", color="positive")],
    [get_button(label="Пары Завтра", color="positive")],
    [get_button(label="Время звонков", color="positive")],
    [get_button(label="Пары на неделю", color="positive")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))



while True:
    try:
    #  главный цикл
        nedelya = datetime.date.today().isocalendar()[1]
        den = datetime.date.today().weekday()
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
        if messages["count"] >= 1:


            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body == "Привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет, друг!"})
            elif body.lower() == "клавиатура":
                vk.method("messages.send", {"peer_id": id, "message": "Выбери кнопку!", "keyboard": keyboard})
            elif body.lower() == "пары":
                vk.method("messages.send", {"peer_id": id, "message": dni(den,nedelya)})
            elif body.lower() == "время звонков":
                vk.method("messages.send", {"peer_id": id, "message": "# пара: начало-конец\n\n1 пара: 9:00-10:30\n2 пара: 10:40-12:10\n3 пара: 13:00-14:30\n4 пара: 14:40-16:10\n5 пара: 16:20-17:50\n6 пара: 18:00-19:30\n7 пара: 18:30-20:00\n8 пара: 20:10-21:40"})
            elif body.lower() == "пары завтра":
                vk.method("messages.send", {"peer_id": id, "message":dni(den+1,nedelya)})
            elif body.lower() == "пары на неделю":
                for i in range(7):
                    vk.method("messages.send", {"peer_id": id, "message": dni(den+i,nedelya)})
            elif body.lower() == "начать":
                vk.method("messages.send", {"peer_id": id, "message": "Начинаем, друг!"})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Я не понял тебя!", "keyboard": keyboard})
        time.sleep(0.5)
    except Exception as E:
        time.sleep(1)

