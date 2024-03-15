import { Router } from 'express'
import { crearPedido } from '../controllers/pedidos.controller.js'
import { validarAdmin, validarToken } from '../validarToken.js'
import AsyncHandler from 'express-async-handler'

export const pedidoRouter = Router()
pedidoRouter.post('/crear-pedido', validarToken, validarAdmin, AsyncHandler(crearPedido))