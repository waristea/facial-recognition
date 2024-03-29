"""empty message

Revision ID: 6d555090b0d1
Revises: 34b7e3d8d59f
Create Date: 2018-04-25 16:59:58.548895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d555090b0d1'
down_revision = '34b7e3d8d59f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.Date(), nullable=False),
    sa.Column('update_on', sa.DateTime(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    # ### end Alembic commands ###
