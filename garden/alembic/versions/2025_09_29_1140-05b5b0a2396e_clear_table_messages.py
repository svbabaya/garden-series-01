"""Clear table messages

Revision ID: 05b5b0a2396e
Revises: 0ca3c4c1f46f
Create Date: 2025-09-29 11:40:24.044625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05b5b0a2396e'
down_revision: Union[str, None] = '0ca3c4c1f46f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    messages = sa.table('messages')
    op.execute(messages.delete())


def downgrade() -> None:
    pass
