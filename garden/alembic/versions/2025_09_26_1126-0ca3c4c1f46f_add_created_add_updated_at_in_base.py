"""Add created_add, updated_at in Base

Revision ID: 0ca3c4c1f46f
Revises: fb878fa3a68a
Create Date: 2025-09-26 11:26:02.922784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ca3c4c1f46f'
down_revision: Union[str, None] = 'fb878fa3a68a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('messages', sa.Column('is_active', sa.Boolean(), nullable=False))


def downgrade() -> None:
    op.drop_column('messages', 'is_active')
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')
