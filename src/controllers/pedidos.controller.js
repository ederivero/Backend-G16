import { EstadoPedido } from '@prisma/client'
import { conexion } from '../conectores.js'
import { crearPedidoDto } from '../dto/pedidos.dto.js'

export const crearPedido = async (req, res) => {
    /**
     * {
     *  clienteId: '12312312',
     *  fecha: '2024-03-13',
     *  direccionId: '123123123123',
     *  detalle: [
     *      {
     *          cantidad: 2,
     *          productoId: '123123123',
     *          precio: 14.5
     *      },
     *      {
     *          cantidad: 1,
     *          productoId: '23232323',
     *          precio: 12.5
     *      },
     *      {
     *          cantidad: 2,
     *          productoId: '345454545',
     *          precio: 20.5
     *      }
     *  ]
     * }
     */
    const validador = crearPedidoDto.validate(req.body)
    if (validador.error) {
        return res.status(400).json({
            message: 'Error al crear el pedido',
            content: validador.error
        })
    }

    await conexion.$transaction(async (cursor) => {
        const { clienteId, fecha, direccionId, detalle } = validador.value

        const nuevoPedido = await cursor.pedido.create({
            data: {
                estado: EstadoPedido.RECIBIDO,
                fecha,
                total: detalle.reduce((valorPrevio, valorActual) => {
                    // valorActual sera toda la informacion del detalle osea {cantidad: ... , productoId:... , precio: ...}
                    return valorPrevio + (valorActual.precio * valorActual.cantidad)
                }, 0),
                clienteId,
                direccionId
            },
            select: {
                // Solamente luego de hacer la creacion devolver el id del pedido creado
                id: true
            }
        })

        await cursor.detallePedido.createMany({
            data: detalle.map((detallePedido) =>
            // Si solamente voy a retornar una linea y esa linea es un JSON entonces en vez de colocar la palabra return puedo prescindir de ella y al JSON colocarlo entre parentesis
            ({
                ...detallePedido,
                pedidoId: nuevoPedido.id,
            })
            )
        })

    })

    return res.status(201).json({
        message: 'Pedido creado exitosamente'
    })
}