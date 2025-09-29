"""Change field author to caption

Revision ID: 5ec7dcd4d5b2
Revises: 05b5b0a2396e
Create Date: 2025-09-30 01:00:34.039761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision: str = '5ec7dcd4d5b2'
down_revision: Union[str, None] = '05b5b0a2396e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('messages')]

    if 'caption' not in columns:
        op.add_column('messages',
                      sa.Column('caption', sa.String(), nullable=False, server_default='')
                      )


def downgrade() -> None:
    conn = op.get_bind()
    inspector = inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('messages')]

    if 'caption' in columns:
        op.drop_column('messages', 'caption')
