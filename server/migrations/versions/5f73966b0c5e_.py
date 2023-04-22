"""empty message

Revision ID: 5f73966b0c5e
Revises: 79f75f806d76
Create Date: 2023-04-10 23:47:01.325148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f73966b0c5e'
down_revision = '79f75f806d76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('units', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('type', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('baths', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('units', schema=None) as batch_op:
        batch_op.drop_column('baths')
        batch_op.drop_column('type')
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###