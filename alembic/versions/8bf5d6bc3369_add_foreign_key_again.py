"""add foreign key again

Revision ID: 8bf5d6bc3369
Revises: d709c250a63d
Create Date: 2025-05-22 20:32:00.273429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bf5d6bc3369'
down_revision: Union[str, None] = 'd709c250a63d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    #op.create_foreign_key('fk_posts_users', 'posts', 'users', ['id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_posts_users', 'posts', type_='foreignkey')
    pass
