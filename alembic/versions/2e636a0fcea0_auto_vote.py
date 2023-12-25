"""auto-vote

Revision ID: 2e636a0fcea0
Revises: 9c9775f3abbb
Create Date: 2023-12-23 18:00:20.642982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector



# revision identifiers, used by Alembic.
revision: str = '2e636a0fcea0'
down_revision: Union[str, None] = '9c9775f3abbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Check if the 'votes' table exists
    inspector = Inspector.from_engine(op.get_bind())
    if 'votes' not in inspector.get_table_names():
        return

    # Add the foreign key constraint
    op.create_foreign_key(
        None, 'votes', 'users', ['user_id'], ['id'], ondelete='CASCADE'
    )

def downgrade():
    op.drop_constraint(None, 'votes', type_='foreignkey')