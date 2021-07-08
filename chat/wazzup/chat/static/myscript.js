//Подключаемся к серверу чата (Любой) ip сервера
let chatServer = new WebSocket('ws://192.168.0.111:3030/')

// обьект для отправки данных на сервер вебсокет
let response = {
    username: 'Bekzat',
    address: 'Ак-Тилек',
    color: 'gold'
}
// когда заходим на сайт отправляем первое сообщение серверу
// когда соединение к серверу успешное
chatServer.onopen = function (event) {
    // отправляем первые данные серверу в JSON формате
    response.message = 'init'
    chatServer.send(JSON.stringify(response))
}

// событье когда сервер нам присылает сообщение
// полученное сообщение рендерим на наш html
chatServer.onmessage = function (event) {
    // получаем контейнер сообщений
    let chatMessageContainer = document.getElementsByClassName(
        'chat-message-container'
    )

    // текущее время
    let time = `
        ${(new Date()).getHours()}
        :
        ${(new Date()).getMinutes()}
    `
    // ИЗ сервера сообщение приходит в JSON формате
    // Мы его преобразуем в JS обьект (как dict python)
    let data = JSON.parse(event.data)
    let direction = 'text-md-end'
    if (
        data.username.toLowerCase()
        === response.username.toLowerCase()
    )
    {
        direction = 'text-md-start'
    }
    // показывем полученное сообщение из сервера в div chat-message-container
     chatMessageContainer[0].innerHTML += `
        <h2 class="${direction} chat-message-parent">
            <div class="chat-author" style="color:${data.color}">
                ${data.username}
            </div>
            <span class="chat-message">
                ${data.message}
                <i class="badge chat-message-time">${time}</i>
            </span>
        </h2>
    `
    // прокрутка вниз когда приходит сообщение
    chatMessageContainer[0].scrollTop =
        chatMessageContainer[0].scrollHeight
    if (
        username.toLowerCase() !== response.username.toLocaleLowerCase()
    ) {
        let audio = new Audio('/static/message-audio.mp3')
        audio.play()
    }
}

// Событье работает когда сервер завершается
chatServer.onclose = function (event) {
    console.log('Соединение завершено', event)
}

// Кнопка ОТПРАВИТЬ
let sendMessageButton = document.getElementById(
    'chat-message-send-button'
)

 // обработчик событье когда
// пользователь нажимает кнопку отправить
function onClickSendButton() {
    // получаем message input
    let messageInput = document.getElementById(
        'chat-message-input'
    )
    // отправляем сообщение из input на сервер в формате JSON
    response.message = messageInput.value
    chatServer.send(JSON.stringify(response))

    // очищаем input после отправки сообщений
    messageInput.value = ''
}

// событье работает когда мы нажимаем на снопка ОТПРАВИТЬ
sendMessageButton.addEventListener('click', onClickSendButton)