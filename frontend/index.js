const socket = io('https://eb84-2800-200-f408-c085-e20e-7d41-ab2e-ad97.ngrok-free.app')

const container = document.getElementById('container')
const nombre = document.getElementById('nombre')
const registrarUsuario = document.getElementById('btnRegistro')

container.classList.add('oculto')
const mensaje = document.getElementById('mensaje')
const mensajes = document.getElementById('mensajes')

let id
// me conecto a mi servidor del socket del backend
socket.on('connect', () => {
    id = socket.id
    console.log(id)
})

// Agregamos el evento cuando se presione Enter al input
mensaje.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const texto = mensaje.value
        // Enviamos a nuestro socket al evento mensaje la informacion necesaria
        socket.emit('mensaje', texto)
        mensaje.value = ''
    }
})

// Ahora si quiero mantenerme escuchando un evento
socket.on('mensajeRecibido', (data) => {
    const div = document.createElement('div')
    const parrafo = document.createElement('p')

    parrafo.innerHTML = `${data.usuario} dice: ${data.mensaje}`
    // Agregar una clase a nuestro parrafo
    parrafo.className = 'burbuja-texto'

    // Dependiendo si es el mismo usuario que esta enviando el mensaje entonces lo colocaremos a la izquierda, caso contrario a la derecha
    div.className = id === data.usuario ? 'izquierda' : 'derecha'

    div.appendChild(parrafo)

    mensajes.appendChild(div)

})