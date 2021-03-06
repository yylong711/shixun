"""empty message

Revision ID: a741cf3e3ce6
Revises: 365634a13409
Create Date: 2018-07-10 10:49:43.463126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a741cf3e3ce6'
down_revision = '365634a13409'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ansj_sentence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=3000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_content', 'ansj_sentence', ['content'], unique=False, mysql_length=50)
    op.create_table('jcseg_sentence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=3000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_content', 'jcseg_sentence', ['content'], unique=False, mysql_length=50)
    op.create_table('ansj_word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=80), nullable=True),
    sa.Column('sentence_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sentence_id'], ['ansj_sentence.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jcseg_word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=80), nullable=True),
    sa.Column('sentence_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sentence_id'], ['jcseg_sentence.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jcseg_word')
    op.drop_table('ansj_word')
    op.drop_index('idx_content', table_name='jcseg_sentence')
    op.drop_table('jcseg_sentence')
    op.drop_index('idx_content', table_name='ansj_sentence')
    op.drop_table('ansj_sentence')
    # ### end Alembic commands ###
