import { Router } from 'express'
import AsyncHandler from 'express-async-handler'
import { crearCategoria, listarCategorias } from '../controllers/categorias.controller.js'

export const categoriaRouter = Router()

categoriaRouter.route('/categoria').post(AsyncHandler(crearCategoria))
categoriaRouter.route('/categorias').get(AsyncHandler(listarCategorias))