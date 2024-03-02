import express from 'express'
import dotenv from 'dotenv'
// Cuando una libreria ha sido desarollada utilizando CommonJS no se puede utilizar la destructuracion en la importacion de EcmaScript porque lanzara un error de incompatibilidad
// Lo mismo si la libreria fue desarrollada en ECMAScript no se puede hacer destructuracion en importaciones de un proyecto en CommonJS
import { PrismaClient } from '@prisma/client'
import Joi from 'joi'
import asyncHandler from 'express-async-handler'

const validacionCategoria = Joi.object({
    nombre: Joi.string().required(),
    habilitado: Joi.boolean().optional()
})

const validacionProducto = Joi.object({
    nombre: Joi.string().required(),
    precio: Joi.number().precision(2).optional(), // Flotante 999.99
    categoriaId: Joi.number().required()
})

// lee las variables del archivo .env 
dotenv.config()
const conexion = new PrismaClient()
const servidor = express()

// nuestro middleware para que acepte json desde el cliente
servidor.use(express.json())

servidor.get('/', (req, res) => {
    res.json({
        message: 'Bienvenido a mi API de minimarket'
    })
})


servidor.route('/categorias').post(asyncHandler(async (req, res) => {
    const resultado = validacionCategoria.validate(req.body)

    if (resultado.error) {
        return res.status(400).json({
            message: 'Error al crear la categoria',
            content: resultado.error
        })
    }
    // Toda las opeaciones con la base de datos siempre se realizaran de manera asincrona
    const categoriaCreada = await conexion.categoria.create({ data: resultado.value }) // {nombre :'abarrotes', habilitado: false}
    console.log(resultado.value)
    console.log(categoriaCreada)
    await conexion.$disconnect() // asi se cierra la conexion con la base de datos en Prisma

    res.json({
        message: 'Categoria creada exitosamente'
    })
})).get(asyncHandler(async (req, res) => {
    const resultado = await conexion.categoria.findMany()

    return res.json({
        content: resultado
    })
}))

servidor.route('/categoria/:id').all(asyncHandler(async (req, res, next) => {
    // Si queremos hacer un mismo paso EN TODOS LOS METODOS DE ESTE ENDPOINT podemos realizarlo en el all
    const { id } = req.params
    // Encontrar si mi categoria existe
    // findFirstOrThrow > me permite filtrar mediante cualquier columna
    // findUniqueOrThrow > me permite filtrar mediante columnas que tenga la propiedad unique (x ejemplo: las PK o @unique)
    // el mas eficiente es el findUniqueOrThrow porque al solo usar las columnas que tengan unicidad hara que la sentencia sea mas optima, PEEERO si tu busqueda incluye una columna no unica entonces ahi si utilizas el findFirstOrThrow

    const parametrosCategoria = req.method === 'GET' ? { id: true, nombre: true, habilitado: true } : { id: true }
    // SELECT id FROM categorias WHERE id = ...;
    // +'Eduardo' > NaN (Not a Number)

    const categoriaEncontrada = await conexion.categoria.findUniqueOrThrow({ where: { id: +id }, select: parametrosCategoria })

    if (req.method === 'PUT') {
        const validacion = validacionCategoria.validate(req.body)

        if (validacion.error) {
            return res.status(400).json({
                message: 'Error al actualizar la categoria',
                content: validacion.error
            })
        }
        req.dataValidada = validacion.value
    }
    // para pasarle alguna informacion adicional a los otros metodos podemos agregarlo al request (req)
    req.categoriaEncontrada = categoriaEncontrada

    // si todo esta bien pasa al metodo que te corresponde
    next()
})).put(asyncHandler(async (req, res) => {
    // validacion.value > {nombre: 'Abarrotes', habilitado: false}
    const categoriaActualizada = await conexion.categoria.update({ where: { id: req.categoriaEncontrada.id }, data: req.dataValidada })

    return res.status(200).json({
        message: 'Categoria actualizada exitosamente',
        content: categoriaActualizada
    })
})).delete(asyncHandler(async (req, res) => {
    await conexion.categoria.delete({ where: { id: req.categoriaEncontrada.id } })

    return res.status(204).send()
})).get(asyncHandler(async (req, res) => {
    return res.json({
        content: req.categoriaEncontrada
    })
}))


servidor.route('/productos').post(asyncHandler(async (req, res) => {
    // Crear un validadorProductos en el cual se le pase el body y retorne la data validada o si es incorrecto el mensaje de error
    const validacion = validacionProducto.validate(req.body)
    if (validacion.error) {
        return res.status(400).json({
            message: 'Error al crear el producto',
            content: validacion.error
        })
    }
    // Con la data validada guardar el producto en la base de datos
    const nuevoProducto = await conexion.producto.create({ data: validacion.value })

    return res.status(201).json({
        message: 'Producto creado exitosamente',
        content: nuevoProducto
    })

})).get(asyncHandler(async (req, res) => {
    // Devolver todos los productos existentes en la base de datos
    const productosEncontrados = await conexion.producto.findMany()

    return res.json({
        content: productosEncontrados
    })
}))

servidor.route('/producto/:id').get(asyncHandler(async (req, res) => {
    const { id } = req.params
    // include > indicar si quiero agregar un modelo adyacente a este
    // no se puede utilizar el include y el select a la vez 
    const productoEncontrado = await conexion.producto.findUniqueOrThrow({
        where: { id: +id },
        // include: {
        //     categoria: true
        // },
        select: {
            id: true,
            nombre: true,
            precio: true,
            categoria: true // si vamos a seleccionar las columnas que queremos mostrar entonces aqui tbn deberemos de poner los modelos que queremos incluir y ya no usar el include
        }
    })

    return res.json({
        content: productoEncontrado
    })
}))

const validacionCategoriaConProductos = Joi.object({
    nombre: Joi.string().required(),
    habilitado: Joi.boolean().optional(),
    productos: Joi.array().items(
        Joi.object({
            nombre: Joi.string().required(),
            precio: Joi.number().precision(2).optional()
        })
    )
})

servidor.post('/crear-categoria-con-productos', asyncHandler(async (req, res) => {
    /*
        {
            nombre: 'Juguetes',
            habilitado: true,
            productos: [
                {
                    nombre: 'Max Steel',
                    precio: 40
                },
                {
                    nombre: 'Barbie Obrera',
                    precio: 45
                }
            ]
        }
    */
    // al tener una serie de operaciones que van a modificar la data en nuestra base de datos se recomienda usar una transaccion
    const validacion = validacionCategoriaConProductos.validate(req.body)

    if (validacion.error) {
        return res.status(400).json({
            message: 'Error al crear la categoria con productos',
            content: validacion.error
        })
    }

    await conexion.$transaction(async (conectorLocal) => {
        // Todo lo que este aca adentro de la transaccion si llega a fallar todas las operaciones de escritura en la bd quedaran sin efecto
        const { productos, nombre, habilitado } = validacion.value

        const nuevaCategoria = await conectorLocal.categoria.create({
            data: {
                nombre,
                habilitado
            }
        })

        // Forma con el uso de FOR (Facil)
        for (let i = 0; i < productos.length; i++) {
            await conectorLocal.producto.create({
                data: {
                    // productos[i] > {nombre: '....' , precio : ....}
                    // nombre: productos[i].nombre,
                    // precio: productos[i].precio,
                    ...productos[i],
                    categoriaId: nuevaCategoria.id
                }
            })
        }
        // Forma usando un map y un create many
        // Esta forma es mas optima porque, ademas de usar un map en vez de un for solamente se hace una peticion a la base de datos con el createMany y se le envian todos los nuevos productos mientras que con la forma anterior por cada insercion se realiza una peticion a la base de datos
        await conectorLocal.producto.createMany({
            data: productos.map((producto) => {
                return {
                    // nombre: producto.nombre,
                    // precio: producto.precio,
                    ...producto,
                    categoriaId: nuevaCategoria.id
                }
            })
        })
    })

    return res.status(201).json({
        message: 'Operacion finalizada exitosamente'
    })
}))









// ------- ZONA MIDDLEWARES ---------------

// Middleware validara que al ya no encontrar mas rutas, entrar a esa por defecto, si lo ponemos antes siempre me iba a devolver este mensaje de error
servidor.use((req, res, next) => {
    res.status(404).json({
        message: 'La ruta que quieres acceder no existe!'
    })
})

// Middleware para capturar los errores (Throw no contrados que lance mi aplicacion)
// Si declaramos 4 parametros en nuestro callback el primero sera el error caso contrario usara el anterior middleware que sera para rutas no existentes
servidor.use((error, req, res, next) => {
    res.status(500).json({
        message: "Error al hacer la peticion",
        content: error.message
    })
})

servidor.listen(process.env.PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})