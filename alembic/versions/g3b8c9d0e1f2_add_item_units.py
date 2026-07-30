"""add shopping-list item units and decimal quantities

Revision ID: g3b8c9d0e1f2
Revises: f2a7b8c9d0e1
Create Date: 2026-07-29

"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "g3b8c9d0e1f2"
down_revision: str | Sequence[str] | None = "f2a7b8c9d0e1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column(
        "shopping_list_items",
        "quantity",
        existing_type=sa.Integer(),
        type_=sa.Numeric(precision=10, scale=2),
        existing_nullable=False,
        postgresql_using="quantity::numeric(10, 2)",
    )
    op.add_column(
        "shopping_list_items",
        sa.Column(
            "unit",
            sa.String(length=20),
            server_default="each",
            nullable=False,
        ),
    )
    op.alter_column(
        "shopping_list_items",
        "unit",
        server_default=None,
    )


def downgrade() -> None:
    op.drop_column("shopping_list_items", "unit")
    op.alter_column(
        "shopping_list_items",
        "quantity",
        existing_type=sa.Numeric(precision=10, scale=2),
        type_=sa.Integer(),
        existing_nullable=False,
        postgresql_using="quantity::integer",
    )
