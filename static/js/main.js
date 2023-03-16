var socket = io();
socket.on('connect', function() {
    console.log('Conectado al servidor de websockets.');
});

socket.on('disconnect', function() {
    console.log('Desconectado del servidor de websockets.');
});

socket.on('chat_message', function(message) {
    var messageList = document.getElementById('messages');
    var messageItem = document.createElement('li');
    messageItem.innerText = message;
    messageItem.className = 'text-white nav p-0 ps-2'
    messageList.appendChild(messageItem);
});

var messageForm = document.getElementById('message-form');
var messageInput = document.getElementById('message-input');

messageForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var message = messageInput.value;
    socket.emit('chat_message', message);
    messageInput.value = '';
});