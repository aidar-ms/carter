"""Added PageSnapshot model

Revision ID: 5e45fc341fd0
Revises: 
Create Date: 2022-02-06 20:19:13.087510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e45fc341fd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page_snapshots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('html_content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('page_snapshots')
    # ### end Alembic commands ###