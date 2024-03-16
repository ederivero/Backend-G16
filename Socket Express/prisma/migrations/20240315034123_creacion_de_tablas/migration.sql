-- CreateTable
CREATE TABLE "usuarios" (
    "id" UUID NOT NULL,
    "nombre" TEXT NOT NULL,
    "socket_id" TEXT NOT NULL,

    CONSTRAINT "usuarios_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "mensajes" (
    "id" UUID NOT NULL,
    "texto" TEXT NOT NULL,
    "usuario_id" UUID NOT NULL,

    CONSTRAINT "mensajes_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "mensajes" ADD CONSTRAINT "mensajes_usuario_id_fkey" FOREIGN KEY ("usuario_id") REFERENCES "usuarios"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
