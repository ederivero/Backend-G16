import { Router } from 'express'
import { registro, login } from '../controllers/usuario.controller.js'
import expressAsyncHandler from 'express-async-handler'

export const usuarioRouter = Router()

usuarioRouter.post('/registro', expressAsyncHandler(registro))
usuarioRouter.post('/login', expressAsyncHandler(login))