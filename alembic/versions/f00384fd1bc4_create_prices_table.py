"""create prices table

Revision ID: f00384fd1bc4
Revises: 
Create Date: 2021-04-08 11:47:23.429779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f00384fd1bc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'price',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('close', sa.Numeric()),
        sa.Column('volume', sa.Numeric()),
        sa.Column('label', sa.Numeric()),
        sa.Column('change', sa.Numeric()),
        sa.Column('change_percent', sa.Numeric())
    )

def downgrade():
    pass
