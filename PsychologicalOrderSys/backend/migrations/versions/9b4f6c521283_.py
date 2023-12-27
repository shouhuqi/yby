"""empty message

Revision ID: 9b4f6c521283
Revises: 75c9f86618ae
Create Date: 2023-11-07 17:08:04.442535

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9b4f6c521283'
down_revision = '75c9f86618ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('orderid', sa.Integer(), nullable=True))
    op.drop_constraint('users_ibfk_1', 'users', type_='foreignkey')
    op.drop_column('users', 'profassionclass')
    op.drop_column('users', 'isbasaceinfo')
    op.drop_column('users', 'schoolid')
    op.drop_column('users', 'isinsider')
    op.drop_column('users', 'nickname')
    op.drop_column('users', 'isreadedrules')
    op.drop_column('users', 'orgid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('orgid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('isreadedrules', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('nickname', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('users', sa.Column('isinsider', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('schoolid', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('users', sa.Column('isbasaceinfo', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('profassionclass', mysql.VARCHAR(length=256), nullable=True))
    op.create_foreign_key('users_ibfk_1', 'users', 'organizations', ['orgid'], ['orgid'])
    op.drop_column('users', 'orderid')
    # ### end Alembic commands ###
