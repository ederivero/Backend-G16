import { Router } from 'express'
import { registro } from '../controllers/usuario.controller.js'
import expressAsyncHandler from 'express-async-handler'

export const usuarioRouter = Router()

usuarioRouter.post('/registro', expressAsyncHandler(registro))