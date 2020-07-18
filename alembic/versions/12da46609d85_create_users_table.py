"""create users table

Revision ID: 12da46609d85
Revises: 
Create Date: 2020-07-18 19:50:20.503239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12da46609d85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'USERS',
        sa.Column('ID', sa.BigInteger(), autoincrement=True, primary_key=True, unique=True, nullable=False),
        sa.Column('LOGIN', sa.String(50), unique=True, nullable=False),
        sa.Column('PASSWORD', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('USERS')
