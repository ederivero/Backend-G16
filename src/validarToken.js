import jwt from 'jsonwebtoken'
import { conexion } from './conectores.js'
import { TipoUsuario } from '@prisma/client'

// middleware para corroborar la validez de la token
export const validarToken = (req, res, next) => {
    // usaremos el header de authorization
    const { authorization } = req.headers
    if (!authorization) {
        // 403 > Forbidden
        return res.status(403).json({
            message: 'Se necesita una token para esta peticion'
        })
    }

    // ahora en el header de authorization tenemos que validar que se envie en el formato Bearer xxxx.yyyy.zzzz
    const token = authorization.split(' ')[1] // ['Bearer', 'xxxxx.yyyy.zzzz']
    if (!token) {
        return res.status(403).json({
            message: 'La token se tiene que enviar usando el formato <Bearer YOUR_TOKEN>'
        })
    }

    // verificara que la token sea correcta, que sea nuestra (por la firma), que siga vigente, cumpla con un formato valido
    try {
        // me devolvera el payload (lo que le agregue al crear la token)
        const payload = jwt.verify(token, process.env.JWT_SECRET_KEY)
        req.user = payload // { usuarioId: '...', tipo: 'ADMIN' }
        // Le indicamos que prosiga con los controladores que vienen luego de este middleware
        next()
    }
    catch (error) {
        return res.status(400).json({
            message: 'Token invalida',
            content: error.message
        })
    }
}

export const validarAdmin = (req, res, next) => {
    // Este middleware tiene que ir luego del validarToken porque en ese middleware agregamos el req.user

    const user = req.user

    if (!user) {
        // primero validamos que tengamos el req.user
        return res.status(500).json({
            message: 'Uso del middleware incorrecto'
        })
    }

    if (user.tipo !== TipoUsuario.ADMIN) {
        // el usuario no es administrador
        return res.status(403).json({
            message: 'Permisos insuficientes'
        })
    }

    next()
}