import { TipoUsuario } from '@prisma/client'
import Joi from 'joi'

export const registroUsuario = Joi.object({
    nombre: Joi.string().required(),
    apellido: Joi.string().required(),
    correo: Joi.string().email().required(),
    password: Joi.string().required(),
    tipoUsuario: Joi.string()
        .valid(TipoUsuario.ADMIN, TipoUsuario.CLIENTE, TipoUsuario.EMPLEADO)
        .default(TipoUsuario.CLIENTE)
})


export const loginUsuario = Joi.object({
    correo: Joi.string().email().required(),
    password: Joi.string().required()
})