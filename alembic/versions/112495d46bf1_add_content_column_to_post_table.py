"""add content column to post table

Revision ID: 112495d46bf1
Revises: c3e678f673be
Create Date: 2023-12-22 19:00:19.138600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '112495d46bf1'
down_revision: Union[str, None] = 'c3e678f673be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
