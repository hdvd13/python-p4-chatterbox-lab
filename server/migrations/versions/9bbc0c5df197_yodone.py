"""yoDone

Revision ID: 9bbc0c5df197
Revises: 916e51e2184f
Create Date: 2023-09-10 11:34:39.217403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bbc0c5df197'
down_revision = '916e51e2184f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('username', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('username')
        batch_op.drop_column('body')

    # ### end Alembic commands ###
