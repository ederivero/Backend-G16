import Joi from "joi";

export const crearPedidoDto = Joi.object({
    clienteId: Joi.string().uuid({ version: 'uuidv4' }).required(),
    fecha: Joi.date().required(),
    direccionId: Joi.string().uuid({ version: 'uuidv4' }),
    detalle: Joi.array().items(Joi.object({
        cantidad: Joi.number().min(0).required(),
        productoId: Joi.string().uuid({ version: 'uuidv4' }).required(),
        precio: Joi.number().precision(2).required()
    }))
})