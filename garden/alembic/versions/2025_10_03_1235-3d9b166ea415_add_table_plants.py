"""Add table user

Revision ID: 3d9b166ea415
Revises: 44e17c2988cd
Create Date: 2025-10-03 12:35:52.629249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d9b166ea415'
down_revision: Union[str, None] = '44e17c2988cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
