"""empty message

Revision ID: 351c7be35783
Revises: b1e3fbfbe7d7
Create Date: 2018-07-19 11:28:28.639364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '351c7be35783'
down_revision = 'b1e3fbfbe7d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_ikanalyzer_word_content'), 'ikanalyzer_word', ['content'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ikanalyzer_word_content'), table_name='ikanalyzer_word')
    # ### end Alembic commands ###
