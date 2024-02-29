import express from 'express'
import morgan from 'morgan'

const servidor = express()
// middleware -> intermediario entre mi peticion del cliente y el controlador final
// indicando a mi servidor que ahora podra recibir los json del body y convertirlos para que puedan ser leidos
servidor.use(express.json()) 
// https://www.npmjs.com/package/morgan#predefined-formats
// tiny > el output mas minima que hay
// METODO URL STATUS_RESPTA TAMAÑO_RPTA - TIEMPO_RPTA

// short > es mas corto que el default pero tbn incluye el tiempo de rpta
// DIRECCION_REMOTA_CLIENTE USUARIO_REMOTO METODO URL HTTP:/VERSION ESTADO_RPTA LONGITUD_CONTENIDO - TIEMPO_RPTA

// dev > Es muy similar al default solo que COLOREA el estado_rpta con color verde para codigos exitosos y rojo para codigos de errores
servidor.use(morgan('dev'))

servidor.get('/',(req, res)=>{
    // para la ruta '/' en el cual respondere con un estado 200 y un json
    return res.status(200).json({
        message:'Bienvenido a mi API de prueba'
    })
})

servidor.route('/empleado').get((req, res)=> {
    return res.json({
        message:'El empleado existe'
    })
}).post((req,res)=>{
    console.log(req.body)

    return res.status(201).json({
        message:'Empleado creado exitosamente'
    })
})

// Para poder reicibir parametros por la url de manera dinamica
servidor.get('/empleado/:id', (req,res)=>{
    const parametros = req.params
    console.log(parametros)

    return res.json({
        message:'ok'
    })
})

// Para poder utilizar query params (llave=valor)
servidor.get('/buscar-empleado', (req,res)=>{
    const parametros = req.query

    console.log(parametros)
    return res.json({
        message:'ok'
    })
})

const empleados = [
    {
        id: 1,
        nombre:'Eduardo',
        apellido:'de Rivero'
    },
    {
        id: 2,
        nombre: 'Javier',
        apellido:'Chuquitaura'
    },
    {
        id: 3,
        nombre:'Roxana',
        apellido:'Melgar'
    },
    {
        id: 4,
        nombre:'Eduardo',
        apellido:'Juarez'
    }
]

// crear un endpoint en el cual se llame filtrar-empleados y en base al nombre pasado como query param devolver todos los empleados con ese filtro



servidor.listen(3000, ()=>{
    console.log('Servidor corriendo exitosamente')
})