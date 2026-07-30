"""remove pricing from products and shopping-list items

Revision ID: e1f6a7b8c9d0
Revises: d0e5f6a7b8c9
Create Date: 2026-07-29

"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "e1f6a7b8c9d0"
down_revision: str | Sequence[str] | None = "d0e5f6a7b8c9"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.drop_column("shopping_list_items", "estimated_price")
    op.drop_column("products", "estimated_price")


def downgrade() -> None:
    op.add_column(
        "products",
        sa.Column(
            "estimated_price",
            sa.Numeric(precision=10, scale=2),
            server_default="0.00",
            nullable=False,
        ),
    )
    op.add_column(
        "shopping_list_items",
        sa.Column(
            "estimated_price",
            sa.Numeric(precision=10, scale=2),
            server_default="0.00",
            nullable=False,
        ),
    )
    op.alter_column(
        "products",
        "estimated_price",
        server_default=None,
    )
    op.alter_column(
        "shopping_list_items",
        "estimated_price",
        server_default=None,
    )
