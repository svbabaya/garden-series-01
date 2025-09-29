"""Del table messages

Revision ID: 44e17c2988cd
Revises: d6a687c7831c
Create Date: 2025-09-30 01:28:49.703466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44e17c2988cd'
down_revision: Union[str, None] = 'd6a687c7831c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.drop_table('messages')


def downgrade() -> None:
    pass
