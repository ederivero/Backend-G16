const BACKEND_URL = 'http://127.0.0.1:3000'
const socket = io(BACKEND_URL)

const container = document.getElementById('container')
const nombre = document.getElementById('nombre')
const registrarUsuario = document.getElementById('btnRegistro')
const registroContainer = document.getElementById('registro')

container.classList.add('oculto')
const mensaje = document.getElementById('mensaje')
const mensajes = document.getElementById('mensajes')

let id
// me conecto a mi servidor del socket del backend
socket.on('connect', () => {
    id = socket.id
    console.log(id)
})

registrarUsuario.addEventListener('click', async (e) => {
    e.preventDefault()

    const resultado = await fetch(`${BACKEND_URL}/crear-usuario`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            socketId: id,
            nombre: nombre.value
        })
    })

    if (resultado.status === 201) {
        const { message } = await resultado.json()
        alert(message)
        // hacemos visible a nuestro contenedor de mensajes
        container.classList.remove('oculto')
        // removemos nuestro contenedor del login
        registroContainer.remove()
    } else {
        alert('Error al crear el usuario')
    }

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

socket.on('historial-mensajes', (data) => {
    console.log(data)
    for (const mensaje of data.mensajes) {
        console.log(mensaje)
        const div = document.createElement('div')
        const parrafo = document.createElement('p')
        parrafo.innerHTML = `${mensaje.usuario.nombre} dice: ${mensaje.texto}`
        // Agregar una clase a nuestro parrafo
        parrafo.className = 'burbuja-texto'
        // Dependiendo si es el mismo usuario que esta enviando el mensaje entonces lo colocaremos a la izquierda, caso contrario a la derecha
        div.className = 'izquierda'

        div.appendChild(parrafo)

        mensajes.appendChild(div)
    }
})