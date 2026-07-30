"""add optional pricing

Revision ID: f2a7b8c9d0e1
Revises: e1f6a7b8c9d0
Create Date: 2026-07-29

"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "f2a7b8c9d0e1"
down_revision: str | Sequence[str] | None = "e1f6a7b8c9d0"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "products",
        sa.Column(
            "estimated_price",
            sa.Numeric(precision=10, scale=2),
            nullable=True,
        ),
    )
    op.add_column(
        "shopping_list_items",
        sa.Column(
            "estimated_price",
            sa.Numeric(precision=10, scale=2),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column("shopping_list_items", "estimated_price")
    op.drop_column("products", "estimated_price")
