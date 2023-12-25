"""add vote table

Revision ID: da2564cba2cd
Revises: 4795197f976f
Create Date: 2023-12-25 18:05:38.900618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da2564cba2cd'
down_revision: Union[str, None] = '4795197f976f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'votes',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('post_id', sa.Integer, sa.ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True),
        # Add other columns as needed
    )

def downgrade():
    op.drop_table('votes')
