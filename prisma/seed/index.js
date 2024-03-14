import { PrismaClient } from '@prisma/client'

const conector = new PrismaClient()

async function main() {
    await conector.categoria.upsert({
        where: {
            nombre: 'Bebidas'
        },
        create: {
            nombre: 'Bebidas'
        }, update: {
            // tbn tengo que declarar los parametros que sean unicos
            nombre: 'Bebidas'
        },
    })
    await conector.categoria.upsert({
        where: {
            nombre: 'Pizzas'
        },
        create: {
            nombre: 'Pizzas'
        },
        update: {
            nombre: 'Pizzas'
        },

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
    await Promise.all(productos.map(async (producto) => {
        let categoria

        if (producto.nombre.includes('Pizza')) {
            categoria = await conector.categoria.findFirstOrThrow({ where: { nombre: { contains: 'Pizza' } }, select: { id: true } })
        } else {
            categoria = await conector.categoria.findFirstOrThrow({ where: { nombre: 'Bebidas' }, select: { id: true } })
        }
        // al retornar un proceso asincrono esto se convertira en una promesa
        return conector.producto.upsert({
            where: { nombre: producto.nombre },
            create: { ...producto, categoriaId: categoria.id },
            update: { ...producto, categoriaId: categoria.id }
        })
    }))

}

main().catch((e) => {
    console.error(e)
})