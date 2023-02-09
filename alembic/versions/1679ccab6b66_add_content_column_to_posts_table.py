"""add content column to posts table

Revision ID: 1679ccab6b66
Revises: 6cbf8c9639fe
Create Date: 2023-02-08 20:57:09.660055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1679ccab6b66'
down_revision = '6cbf8c9639fe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content') 
    pass
