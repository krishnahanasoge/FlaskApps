"""empty message

Revision ID: 28f254ccc0af
Revises: e794e2061889
Create Date: 2020-04-28 23:18:07.867543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f254ccc0af'
down_revision = 'e794e2061889'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('lilst_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'todos', 'todolists', ['lilst_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'lilst_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###