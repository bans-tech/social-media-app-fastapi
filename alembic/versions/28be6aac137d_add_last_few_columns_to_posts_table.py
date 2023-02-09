"""add last few columns to posts table

Revision ID: 28be6aac137d
Revises: bbacb0c041f5
Create Date: 2023-02-08 22:49:09.640058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28be6aac137d'
down_revision = 'bbacb0c041f5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
