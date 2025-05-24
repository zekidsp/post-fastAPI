"""create posts table

Revision ID: 6e44117b4305
Revises: 
Create Date: 2025-05-22 19:28:51.475312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e44117b4305'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String, nullable=False),
        #sa.Column("content", sa.String, nullable=False),
        #sa.Column("published", sa.Boolean, server_default='TRUE'),
        #sa.Column("created_at", sa.TIMESTAMP, server_default=sa.text('now()'), nullable=False),
        #sa.Column("owner_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
    pass
