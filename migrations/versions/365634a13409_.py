"""empty message

Revision ID: 365634a13409
Revises: 2c453b3f95a9
Create Date: 2018-07-10 10:34:05.694341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '365634a13409'
down_revision = '2c453b3f95a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_content', 'jieba_sentence', ['content'], unique=False, mysql_length=50)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_content', table_name='jieba_sentence')
    # ### end Alembic commands ###