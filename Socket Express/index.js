import express from 'express'
import { Server } from 'socket.io'
// Libreria que sirve para crear un servidor de la forma mas basica sin usar express u otros es lo que utiliza socket.io para poder funcionar
import { createServer } from 'http'
import { PrismaClient } from '@prisma/client'
import cors from 'cors'

const conector = new PrismaClient({ datasources: { db: { url: process.env.DATABASE_URL3 } } })

const servidor = express()
// Nuestro servidor base sera el del http pero internamente tbn utilizaremos express para facilitar las cosas porque la libreria http hace los metodos y rutas mas complicadas que express
const servidorHTTP = createServer(servidor)

// Los cors configurados en nuestro servidor pueden tener diferente configuracion que los del socket
const servidorSocket = new Server(servidorHTTP, { cors: { origin: '*' } })

servidor.use(express.json())
// Estos cors no son los mismos que los cors declarados en el socket, ya que son diferentes tipos de comunicacion con mi backend uno es x sockets y el otro por http request
servidor.use(cors({ allowedHeaders: ['Content-Type', 'Authorization', 'accepts'], methods: ['POST', 'GET'], origin: '*' }))


servidor.post('/crear-usuario', async (req, res) => {
    const { socketId, nombre } = req.body

    console.log(req.body)
    await conector.usuario.create({ data: { socketId, nombre } })

    return res.status(201).json({
        message: 'Usuario creado exitosamente'
    })
})

const obtenerMensajes = async () => {
    const mensajes = await conector.mensaje.findMany({ include: { usuario: true } })
    console.log(mensajes)
    return { mensajes }
}


// Cuando un usuario se quiera conectar a mi servidor de socket este lo hara por el metodo 'on' mediante el evento 'connection'
servidorSocket.on('connection', async (cliente) => {
    console.log(cliente.id)

    cliente.emit('saludo', { message: 'Bienvenido a mi Socket de NodeJs' })

    // cuando el usuario se conecte al servidor de socket vamos a retornar todos los mensajes en la base de datos
    cliente.emit('historial-mensajes', await obtenerMensajes())
    // ahora escucharemos un evento que nos enviara el cliente
    cliente.on('mensaje', async (texto) => {
        console.log(texto)
        // vamos a agregar el mensaje a la base de datos
        const usuarioEncontrado = await conector.usuario.findFirst({ where: { socketId: cliente.id } })
        if (!usuarioEncontrado) {
            console.log('El usuario no existe!')
        }
        else {
            await conector.mensaje.create({
                data: { texto, usuarioId: usuarioEncontrado.id }
            })
        }
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