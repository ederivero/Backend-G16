import express from 'express'
import mongoose from 'mongoose'

const servidor = express()

servidor.use(express.json())


// estas configuraciones solamente sirve cuando usemos mongoose ya que si nos vamos directamente a la base de datos todas estas validaciones quedaran sin efecto
const contactoSchema = new mongoose.Schema({
    nombre: {
        // https://mongoosejs.com/docs/guide.html
        type: mongoose.Schema.Types.String,
        // https://mongoosejs.com/docs/schematypes.html#schematype-options
        required: true,
        maxLength: 50
    },
    telefono: {
        type: mongoose.Schema.Types.String,
        required: true
    }
})

// Ahora lo registro en mi base de datos
const ContactoModel = mongoose.model('contactos', contactoSchema)

servidor.listen(process.env.PORT, async () => {
    await mongoose.connect(process.env.MONGODB_URL)
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})