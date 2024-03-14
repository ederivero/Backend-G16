import { Router } from 'express'
import { crearPedido } from '../controllers/pedidos.controller.js'
import { validarToken } from '../validarToken.js'
import AsyncHandler from 'express-async-handler'

export const pedidoRouter = Router()
pedidoRouter.post('/crear-pedido', validarToken, validarToken, AsyncHandler(crearPedido))