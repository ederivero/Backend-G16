import { PrismaClient } from '@prisma/client'

// export const conexion1 = new PrismaClient({datasources: 'mysql://usuario:password@host:3306/my_db'})

export const conexion = new PrismaClient({
    datasources: {
        db: { url: process.env.DATABASE_URL2 }
    }
})