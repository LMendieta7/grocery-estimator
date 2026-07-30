"""add shopping-list item category and estimated price

Revision ID: d0e5f6a7b8c9
Revises: c9d4e5f6a7b8
Create Date: 2026-07-29

"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "d0e5f6a7b8c9"
down_revision: str | Sequence[str] | None = "c9d4e5f6a7b8"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "shopping_list_items",
        sa.Column("category_id", sa.Integer(), nullable=True),
    )
    op.add_column(
        "shopping_list_items",
        sa.Column(
            "estimated_price",
            sa.Numeric(precision=10, scale=2),
            nullable=True,
        ),
    )
    op.create_foreign_key(
        "fk_shopping_list_items_category_id_categories",
        "shopping_list_items",
        "categories",
        ["category_id"],
        ["id"],
    )

    op.execute(
        """
        UPDATE shopping_list_items AS list_item
        SET
            category_id = product.category_id,
            estimated_price = product.estimated_price
        FROM products AS product
        WHERE list_item.product_id = product.id
        """
    )

    op.alter_column(
        "shopping_list_items",
        "category_id",
        existing_type=sa.Integer(),
        nullable=False,
    )
    op.alter_column(
        "shopping_list_items",
        "estimated_price",
        existing_type=sa.Numeric(precision=10, scale=2),
        nullable=False,
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_shopping_list_items_category_id_categories",
        "shopping_list_items",
        type_="foreignkey",
    )
    op.drop_column("shopping_list_items", "estimated_price")
    op.drop_column("shopping_list_items", "category_id")
