import { conexion } from '../conectores.js'
import { crearCategoriaDto } from '../dto/categorias.dto.js'

export async function crearCategoria(req, res) {
    console.log(process.env.DATABASE_URL)
    console.log(process.env.JWT_SECRET_KEY)
    const validacion = crearCategoriaDto.validate(req.body)

    if (validacion.error) {
        return res.status(400).json({
            content: validacion.error
        })
    }

    const categoriaCreada = await conexion.categoria.create({ data: validacion.value })

    return res.status(201).json({
        message: 'Categoria creada exitosamente',
        content: categoriaCreada
    })
}