import { Router } from 'express'
import AsyncHandler from 'express-async-handler'
import { crearCategoria, listarCategorias } from '../controllers/categorias.controller.js'
import { validarAdmin, validarToken } from '../validarToken.js'

export const categoriaRouter = Router()

categoriaRouter.route('/categoria').post(validarToken, validarAdmin, AsyncHandler(crearCategoria))
categoriaRouter.route('/categorias').get(AsyncHandler(listarCategorias))