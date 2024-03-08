import { conexion } from '../conectores.js'
import { registroUsuario } from '../dto/usuario.dto.js'
import bcryptjs from 'bcryptjs'

export const registro = async (req, res) => {
    const validacion = registroUsuario.validate(req.body)

    if (validacion.error) {
        return res.status(400).json({
            message: 'Error al registrar al usuario',
            coontent: validacion.error
        })
    }

    // generamos el texto aleatorio que se fusionara con la password
    const salt = await bcryptjs.genSalt()

    // ahora combinamos el salt con la password para que no retorne el hash de la password
    const passwordHashed = await bcryptjs.hash(validacion.value.password, salt)

    const nuevoUsuario = await conexion.usuario.create({
        // le pasamos todo el CONTENIDO (...) de nuestro validacion.value y luego le modificamos la password
        // esto tiene que ir al final porque si lo ponemos al comienzo se sobreescribira con lo que esta en validacion.value
        data: { ...validacion.value, password: passwordHashed }
    })

    return res.status(201).json({
        message: 'Usuario creado exitosamente',
        content: nuevoUsuario
    })

}