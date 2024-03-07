import express from 'express'
const servidor = express()

servidor.use(express.json())

servidor.listen(process.env.PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})