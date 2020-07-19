"""add test data to users

Revision ID: 37503f88f36d
Revises: 12da46609d85
Create Date: 2020-07-19 11:17:27.668511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37503f88f36d'
down_revision = '12da46609d85'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO "USERS" ("LOGIN", "PASSWORD") VALUES ('Alex123', '123'); 
        INSERT INTO "USERS" ("LOGIN", "PASSWORD") VALUES ('mikebike', '123');
        INSERT INTO "USERS" ("LOGIN", "PASSWORD") VALUES ('Egor', '12345')
        """
    )


def downgrade():
    op.execute('TRUNCATE TABLE "USERS"')
