"""remove notes from products

Revision ID: b8c3d4e5f6a7
Revises: 6c11a88a3942
Create Date: 2026-07-26

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b8c3d4e5f6a7"
down_revision: Union[str, Sequence[str], None] = "6c11a88a3942"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("products", "notes")


def downgrade() -> None:
    op.add_column(
        "products",
        sa.Column("notes", sa.Text(), nullable=True),
    )
