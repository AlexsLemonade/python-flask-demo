"""Second migration.

Revision ID: 693c804233bd
Revises: 887d0e64a1c4
Create Date: 2020-02-04 17:46:28.494115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693c804233bd'
down_revision = '887d0e64a1c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'organizations', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'organizations', type_='unique')
    # ### end Alembic commands ###
