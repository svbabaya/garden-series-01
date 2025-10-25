"""add data in db

Revision ID: b3895dcd698f
Revises: 424f0bb37a75
Create Date: 2025-10-25 12:50:11.227912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3895dcd698f'
down_revision: Union[str, None] = '424f0bb37a75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
