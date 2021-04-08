"""create stocks table

Revision ID: b72ceff35123
Revises: f00384fd1bc4
Create Date: 2021-04-08 16:37:23.696819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b72ceff35123'
down_revision = 'f00384fd1bc4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stocks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('close', sa.Numeric(10,2)),
        sa.Column('volume', sa.Numeric(10,2)),
        sa.Column('label', sa.String(15)),
        sa.Column('change', sa.Numeric(10,2)),
        sa.Column('change_percent', sa.Numeric(10,2))
    )


def downgrade():
    pass
