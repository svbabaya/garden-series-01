"""create table messages

Revision ID: dd82f6c39003
Revises: 
Create Date: 2025-09-26 00:22:19.048282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd82f6c39003'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('messages',
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('mode', sa.Enum('ORDINARY', name='mode'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_displayed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('text')
    )


def downgrade() -> None:
    op.drop_table('messages')
