"""foreign key to psot table 

Revision ID: 16b331f539ea
Revises: bd10d2485752
Create Date: 2025-05-22 20:18:35.025771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16b331f539ea'
down_revision: Union[str, None] = 'bd10d2485752'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    #op.add_column('posts', sa.Column('owner_id', sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False))
    op.create_foreign_key('fk_posts_users', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_posts_users', 'posts', type_='foreignkey')
    #op.drop_column('posts', 'owner_id')
    pass
