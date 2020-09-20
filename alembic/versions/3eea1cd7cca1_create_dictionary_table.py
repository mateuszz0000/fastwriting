"""Create Dictionary table

Revision ID: 3eea1cd7cca1
Revises: c66d90aedbda
Create Date: 2020-09-20 16:22:22.049587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eea1cd7cca1'
down_revision = 'c66d90aedbda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dictionary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=100), nullable=True),
    sa.Column('lang', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lang'], ['language.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dictionary_id'), 'dictionary', ['id'], unique=False)
    op.create_index(op.f('ix_dictionary_lang'), 'dictionary', ['lang'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dictionary_lang'), table_name='dictionary')
    op.drop_index(op.f('ix_dictionary_id'), table_name='dictionary')
    op.drop_table('dictionary')
    # ### end Alembic commands ###