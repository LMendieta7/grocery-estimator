"""make shopping-list names unique

Revision ID: j6e1f2a3b4c5
Revises: i5d0e1f2a3b4
Create Date: 2026-08-02

"""

from collections.abc import Sequence

from alembic import op


revision: str = "j6e1f2a3b4c5"
down_revision: str | Sequence[str] | None = "i5d0e1f2a3b4"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_unique_constraint(
        "uq_shopping_lists_name",
        "shopping_lists",
        ["name"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "uq_shopping_lists_name",
        "shopping_lists",
        type_="unique",
    )
