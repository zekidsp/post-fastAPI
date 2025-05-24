"""add last few columns to post table

Revision ID: d709c250a63d
Revises: 16b331f539ea
Create Date: 2025-05-22 20:26:06.053780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd709c250a63d'
down_revision: Union[str, None] = '16b331f539ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP, server_default=sa.text('now()'), nullable=False))
    #op.create_foreign_key('fk_posts_users', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    #op.drop_constraint('fk_posts_users', 'posts', type_='foreignkey')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    pass
