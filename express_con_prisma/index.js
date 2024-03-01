import express from 'express'
import dotenv from 'dotenv'
// Cuando una libreria ha sido desarollada utilizando CommonJS no se puede utilizar la destructuracion en la importacion de EcmaScript porque lanzara un error de incompatibilidad
// Lo mismo si la libreria fue desarrollada en ECMAScript no se puede hacer destructuracion en importaciones de un proyecto en CommonJS
import {PrismaClient} from '@prisma/client'
import Joi from 'joi'

const validacionCategoria = Joi.object({
    nombre: Joi.string().required(),
    habilitado: Joi.boolean().optional()
})

// lee las variables del archivo .env 
dotenv.config()
const conexion = new PrismaClient()
const servidor = express()

// nuestro middleware para que acepte json desde el cliente
servidor.use(express.json())

servidor.get('/',(req,res)=>{
    res.json({
        message:'Bienvenido a mi API de minimarket'
    })
})


servidor.post('/categorias', async (req,res)=>{
    const resultado = validacionCategoria.validate(req.body)
    
    if(resultado.error){
        return res.status(400).json({
            message:'Error al crear la categoria',
            content: resultado.error
        })
    }
    // Toda las opeaciones con la base de datos siempre se realizaran de manera asincrona
    const categoriaCreada = await conexion.categoria.create({data: resultado.value}) // {nombre :'abarrotes', habilitado: false}
    console.log(resultado.value)
    console.log(categoriaCreada)
    await conexion.$disconnect() // asi se cierra la conexion con la base de datos en Prisma

    res.json({
        message:'Categoria creada exitosamente'
    })
})


// Middleware validara que al ya no encontrar mas rutas, entrar a esa por defecto, si lo ponemos antes siempre me iba a devolver este mensaje de error
servidor.use((req,res,next)=>{
    res.status(404).json({
        message:'La ruta que quieres acceder no existe!'
    })
})

servidor.listen(process.env.PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})