import websockets
import asyncio
import json

# Здесь храним подключенным к серверу клиентов
users = set()

async def message(websocket, path):
    while True:

        # получаем сообщение из бекэнда
        json_response = await websocket.recv()

        # Преобразуем JSON ответ в dict
        response_dict = json.loads(json_response)

        # выводим сообщение клиента для дебага
        print('Message: ', response_dict['message'])
        if response_dict['message'] == 'init':
            # Когда пользователь впервые подключается мы его запоминаем
            user.add(websocket)
            for user in users:
                response_dict['message'] = 'Вошел'
                if user.closed == False:
                    await user.send(json.dump(response_dict))
        else:
            # заново отправляем сообщение клиенту
            for user in users:
                if user.closed == False:
                    await user.send(json_response)



server = websockets.serve(message, port=3030)

print('Our web chat server is run...')

# Запуск сервера веб чата
asyncio.get_event_loop().run_until_complete(server)

# запуск сервера постоянно
asyncio.get_event_loop().run_forever()