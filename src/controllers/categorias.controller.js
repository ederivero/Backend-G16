import { conexion } from '../conectores.js'
import { crearCategoriaDto } from '../dto/categorias.dto.js'

export async function crearCategoria(req, res) {
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

export async function listarCategorias(req, res) {
    // Devolver todas las categorias
    const categorias = await conexion.categoria.findMany()

    return res.json({
        content: categorias
    })
}