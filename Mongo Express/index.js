import express from 'express'
import mongoose from 'mongoose'
import Joi from 'joi'

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

const validarContactoDto = Joi.object({
    nombre: Joi.string().required(),
    telefono: Joi.string().required()
})

servidor.route('/contactos').post(async (req, res) => {
    const validador = validarContactoDto.validate(req.body)

    if (validador.error) {
        return res.status(400).json({
            message: 'Error al crear el contacto',
            content: validador.error
        })
    }

    const contactoCreado = await ContactoModel.create(validador.value)

    return res.status(201).json({
        message: 'Contacto creado exitosamente',
        content: contactoCreado.toJSON() // toJson() > utiliza los metodos que hemos declarado en cada columna para el get 
        // si no se utiliza el metodo toJson() entonces devolvera la informacion sin hacer la conversion definida en la propiedad transform 
    })

}).get(async (req, res) => {
    const contactos = await ContactoModel.find()
    // retornara una lista de contactos por lo que podremos iterarla
    return res.json({
        content: contactos.map((contacto) => contacto.toJSON()) // itero mi arreglo de contactos y en cada uno de ellos utilizo el metodo toJSON que devolvera la info parseada
    })
})

servidor.route('/contacto/:id').all(async (req, res, next) => {
    const { id } = req.params
    // validamos si el id es un objectId (el id que maneja mongo)
    const objectIdValido = mongoose.Types.ObjectId.isValid(id)
    if (!objectIdValido) {
        // Si el objectId es invalido entonces lanzara un error en vez de retornar que el contacto no existe
        return res.status(400).json({
            message: 'El id es invalido'
        })
    }
    next()
}).get(async (req, res) => {
    const { id } = req.params

    const contactoEncontrado = await ContactoModel.findById(id)

    if (!contactoEncontrado) {
        return res.status(404).json({
            message: 'El contacto no existe'
        })
    } else {
        return res.json({
            content: contactoEncontrado.toJSON()
        })
    }
}).put(async (req, res) => {
    const { id } = req.params

    const validador = validarContactoDto.validate(req.body)

    if (validador.error) {
        return res.status(400).json({
            message: 'Error al actualizar el contacto'
        })
    }
    // https://mongoosejs.com/docs/api/model.html#Model.findByIdAndUpdate()
    const resultado = await ContactoModel.findByIdAndUpdate(id, validador.value, { returnDocument: 'after' })

    return res.json({
        message: 'Contacto actualizado exitosamente',
        content: resultado
    })
}).delete(async (req, res) => {
    const { id } = req.params

    // https://mongoosejs.com/docs/api/model.html#Model.findByIdAndDelete()
    const resultado = await ContactoModel.findByIdAndDelete(id)

    console.log(resultado)
    return res.status(204).send()
})


servidor.route('/buscar-contactos').get(async (req, res) => {
    const { nombre, telefono } = req.query

    const filtros = {}

    if (nombre) {
        // .*NOMBRE.* > .* no importa lo que este antes o despues del texto
        // si queremos que la busqueda del nombre de insensitive (no distinga entre mayus o minus) colocaremos la opcion 'i'
        // SELECT * FROM contactos WHERE nombre LIKE '....';
        filtros.nombre = { $regex: `.*${nombre}.*`, $options: 'i' }
    }

    if (telefono) {
        filtros.telefono = telefono
    }

    const contactosEncontrados = await ContactoModel.find(filtros)

    return res.json({
        content: contactosEncontrados.map(contacto => contacto.toJSON())
    })
})




servidor.listen(process.env.PORT, async () => {
    await mongoose.connect(process.env.MONGODB_URL)
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})