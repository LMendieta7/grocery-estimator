"""rename shopping-list item name

Revision ID: c9d4e5f6a7b8
Revises: b8c3d4e5f6a7
Create Date: 2026-07-29

"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "c9d4e5f6a7b8"
down_revision: str | Sequence[str] | None = "b8c3d4e5f6a7"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column(
        "shopping_list_items",
        "product_name_snapshot",
        new_column_name="name",
        existing_type=sa.Text(),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "shopping_list_items",
        "name",
        new_column_name="product_name_snapshot",
        existing_type=sa.Text(),
        existing_nullable=False,
    )
