"""empty message

Revision ID: 34b7e3d8d59f
Revises: bad4b8a6b31d
Create Date: 2018-04-25 01:25:21.630757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34b7e3d8d59f'
down_revision = 'bad4b8a6b31d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('presence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('updated_on', sa.DateTime(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('is_present', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('presence')
    # ### end Alembic commands ###