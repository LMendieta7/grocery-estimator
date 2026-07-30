"""remove pricing from shared products

Revision ID: h4c9d0e1f2a3
Revises: g3b8c9d0e1f2
Create Date: 2026-07-29

"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "h4c9d0e1f2a3"
down_revision: str | Sequence[str] | None = "g3b8c9d0e1f2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.drop_column("products", "estimated_price")


def downgrade() -> None:
    op.add_column(
        "products",
        sa.Column(
            "estimated_price",
            sa.Numeric(precision=10, scale=2),
            nullable=True,
        ),
    )
