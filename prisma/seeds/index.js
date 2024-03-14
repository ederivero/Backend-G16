import { PrismaClient } from '@prisma/client'
import { conexion } from '../../src/conectores'

const conector = new PrismaClient()

async function main() {
    await conector.categoria.upsert({
        create: {
            nombre: 'Bebidas'
        }, update: {}, where: {
            nombre: 'Bedidas'
        }
    })
    await conector.categoria.upsert({
        create: {
            nombre: 'Pizzas'
        },
        update: {},
        where: {
            nombre: 'Pizzas'
        }
    })

    const productos = [{
        nombre: 'Pizza napolitana',
        precio: 20.4,
        disponibilidad: true,
        descripcion: 'Deliciosa pizza con tomate y queso peperoni',
    }, {
        nombre: 'Kola Real 2 Ltrs.',
        precio: 7.20,
        disponibilidad: true,
    }, {
        nombre: 'Pizza Capresse',
        precio: 35.20,
        disponibilidad: true,
        descripcion: 'Exquisita pizza con albhaca y poro'
    }]

    // Si todas las promesas se ejecutan correctamente entonces funcionara todo ok, si una de ellas falla entonces todo fallara
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
    const resultado = await Promise.all(productos.map(async (producto) => {
        let categoria

        if (producto.nombre.includes('Pizza')) {
            categoria = await conector.categoria.findFirstOrThrow({ where: { nombre: { contains: 'Pizza' } }, select: { id: true } })
        } else {
            categoria = await conector.categoria.findFirstOrThrow({ where: { nombre: 'Bebidas' }, select: { id: true } })
        }

        return { ...producto, categoriaId: categoria.id }
    }))

    await conector.producto.createMany({ data: resultado })


}