import asyncio
import websockets

server_url = 'ws://127.0.0.1:3030'
async def client_message():
    # Подключаемся к серверу асинхронный код
    async with websockets.connect(server_url) as websocket:
        message = input('Your message here: ')
        await websocket.send(message)
        print('message sent')

asyncio.get_event_loop().run_until_complete(client_message())