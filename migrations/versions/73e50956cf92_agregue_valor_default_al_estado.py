"""agregue valor default al estado

Revision ID: 73e50956cf92
Revises: bfc516a8d30e
Create Date: 2024-02-08 19:30:47.561473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73e50956cf92'
down_revision = 'bfc516a8d30e'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='pedidos', column_name='estado',
                    server_default='EN_ESPERA')


def downgrade():
    op.alter_column(table_name='pedidos',
                    column_name='estado', server_default=None)
