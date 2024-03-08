import express from 'express'
import * as Rutas from './router/categoria.router.js'

const servidor = express()

servidor.use(express.json())


// Cuando queremos agregar un conjunto de rutas a nuestra aplicacion utilizamos el middleware `use` que indicara las subrutas disponibles
servidor.use(Rutas.categoriaRouter)

servidor.listen(process.env.PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})