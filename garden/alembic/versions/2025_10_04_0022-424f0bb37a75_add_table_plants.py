"""Add table user

Revision ID: 424f0bb37a75
Revises: 3d9b166ea415
Create Date: 2025-10-04 00:22:59.016100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '424f0bb37a75'
down_revision: Union[str, None] = '3d9b166ea415'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
