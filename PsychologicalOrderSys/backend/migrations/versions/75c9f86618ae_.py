"""empty message

Revision ID: 75c9f86618ae
Revises: 
Create Date: 2023-11-06 20:39:44.757645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75c9f86618ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('managers',
    sa.Column('mid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mlevel', sa.Integer(), nullable=True),
    sa.Column('mname', sa.String(length=64), nullable=False),
    sa.Column('mpassword', sa.String(length=128), nullable=False),
    sa.Column('mphonenum', sa.String(length=15), nullable=False),
    sa.Column('m2org', sa.Integer(), nullable=False),
    sa.Column('isdelet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('mid')
    )
    op.create_table('organizations',
    sa.Column('orgid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('orgname', sa.String(length=64), nullable=True),
    sa.Column('isdelet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('orgid')
    )
    op.create_table('rule',
    sa.Column('ruid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rutext', sa.String(length=2048), nullable=True),
    sa.Column('isdelet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ruid')
    )
    op.create_table('swiper',
    sa.Column('sid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('surl', sa.String(length=1024), nullable=True),
    sa.Column('isdelet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_table('rooms',
    sa.Column('rid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rname', sa.String(length=64), nullable=False),
    sa.Column('raddress', sa.String(length=512), nullable=False),
    sa.Column('rdescribe', sa.String(length=512), nullable=False),
    sa.Column('rphotoURL', sa.String(length=1024), nullable=True),
    sa.Column('pdfname', sa.String(length=1024), nullable=True),
    sa.Column('pdfurl', sa.String(length=1024), nullable=True),
    sa.Column('rcanbeusetimes', sa.String(length=512), nullable=True),
    sa.Column('orgid', sa.Integer(), nullable=False),
    sa.Column('isdelet', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['orgid'], ['organizations.orgid'], ),
    sa.PrimaryKeyConstraint('rid')
    )
    op.create_table('users',
    sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uopenid', sa.String(length=64), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('avatarUrl', sa.String(length=1024), nullable=True),
    sa.Column('uname', sa.String(length=64), nullable=True),
    sa.Column('uphonenum', sa.String(length=15), nullable=True),
    sa.Column('schoolid', sa.String(length=64), nullable=True),
    sa.Column('profassionclass', sa.String(length=256), nullable=True),
    sa.Column('orgid', sa.Integer(), nullable=True),
    sa.Column('isinsider', sa.Integer(), nullable=True),
    sa.Column('isbasaceinfo', sa.Integer(), nullable=True),
    sa.Column('isreadedrules', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['orgid'], ['organizations.orgid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('orderitems',
    sa.Column('oid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('odatetime', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('room2orgid', sa.Integer(), nullable=False),
    sa.Column('usingtime', sa.String(length=64), nullable=True),
    sa.Column('roomusage', sa.String(length=1024), nullable=False),
    sa.Column('autograph', sa.String(length=1024), nullable=True),
    sa.Column('rejectreasion', sa.String(length=512), nullable=True),
    sa.Column('checker_id', sa.Integer(), nullable=True),
    sa.Column('ostatus', sa.Integer(), nullable=True),
    sa.Column('ochecktime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['checker_id'], ['managers.mid'], ),
    sa.ForeignKeyConstraint(['room2orgid'], ['organizations.orgid'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.rid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('oid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderitems')
    op.drop_table('users')
    op.drop_table('rooms')
    op.drop_table('swiper')
    op.drop_table('rule')
    op.drop_table('organizations')
    op.drop_table('managers')
    # ### end Alembic commands ###