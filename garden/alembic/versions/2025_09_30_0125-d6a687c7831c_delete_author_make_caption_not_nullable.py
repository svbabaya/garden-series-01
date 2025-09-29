"""Delete author, make caption not nullable

Revision ID: d6a687c7831c
Revises: 5ec7dcd4d5b2
Create Date: 2025-09-30 01:25:35.316846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6a687c7831c'
down_revision: Union[str, None] = '5ec7dcd4d5b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Для SQLite нужно быть осторожным с ALTER TABLE

    # 1. Сначала обрабатываем caption
    op.execute("UPDATE messages SET caption = '' WHERE caption IS NULL")
    with op.batch_alter_table('messages') as batch_op:
        batch_op.alter_column('caption', nullable=False, server_default='')

    # 2. Удаляем author
    with op.batch_alter_table('messages') as batch_op:
        batch_op.drop_column('author')


def downgrade():
    # Восстанавливаем в обратном порядке
    with op.batch_alter_table('messages') as batch_op:
        batch_op.add_column(sa.Column('author', sa.String(), nullable=True))
        batch_op.alter_column('caption', nullable=True, server_default=None)
