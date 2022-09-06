"""add content column to posts table

Revision ID: e78b9732b6e9
Revises: eea5c6a79736
Create Date: 2022-09-06 14:54:49.320994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e78b9732b6e9'
down_revision = 'eea5c6a79736'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
