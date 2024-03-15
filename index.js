import express from 'express'
import { Server } from 'socket.io'
// Libreria que sirve para crear un servidor de la forma mas basica sin usar express u otros es lo que utiliza socket.io para poder funcionar
import { createServer } from 'http'

const servidor = express()
// Nuestro servidor base sera el del http pero internamente tbn utilizaremos express para facilitar las cosas porque la libreria http hace los metodos y rutas mas complicadas que express
const servidorHTTP = createServer(servidor)

// Los cors configurados en nuestro servidor pueden tener diferente configuracion que los del socket
const servidorSocket = new Server(servidorHTTP, { cors: { origin: '*' } })

// Cuando un usuario se quiera conectar a mi servidor de socket este lo hara por el metodo 'on' mediante el evento 'connection'
servidorSocket.on('connection', (cliente) => {
    console.log(cliente.id)

    cliente.emit('saludo', { message: 'Bienvenido a mi Socket de NodeJs' })

    // ahora escucharemos un evento que nos enviara el cliente
    cliente.on('mensaje', (texto) => {
        console.log(texto)

        // usamos el broadcast para enviar el mensaje llegado hacia los demas participantes
        servidorSocket.emit('mensajeRecibido', {
            usuario: cliente.id,
            mensaje: texto
        })
        // si solamente me quiero enviar a mi mismo el mensaje que acabo de enviar 
        cliente.emit('mensaje_recibido_a_mi_mismo', {
            usuario: cliente.id,
            mensaje: texto
        })
    })
})

servidorHTTP.listen(process.env.PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})