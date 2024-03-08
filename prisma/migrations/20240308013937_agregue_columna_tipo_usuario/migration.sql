-- CreateEnum
CREATE TYPE "TipoUsuario" AS ENUM ('ADMIN', 'EMPLEADO', 'CLIENTE');

-- AlterTable
ALTER TABLE "usuarios" ADD COLUMN     "tipo_usuario" "TipoUsuario" NOT NULL DEFAULT 'CLIENTE';
