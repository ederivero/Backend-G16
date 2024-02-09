"""modificar estado a los pedidos antiguos

Revision ID: 4f99ba15b648
Revises: 73e50956cf92
Create Date: 2024-02-08 19:38:22.449420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f99ba15b648'
down_revision = '73e50956cf92'
branch_labels = None
depends_on = None


def upgrade():
    # Si queremos realizar en la migracion un comando de ejecucion SQL podemos usar el metodo execute
    op.execute("UPDATE pedidos SET estado = 'EN_ESPERA' WHERE estado IS NULL")


def downgrade():
    pass
