import { Router } from 'express'
import AsyncHandler from 'express-async-handler'
import { crearCategoria } from '../controllers/categorias.js'

export const categoriaRouter = Router()

categoriaRouter.route('/categoria').post(AsyncHandler(crearCategoria))