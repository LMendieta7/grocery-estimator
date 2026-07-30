"""move images from products to shopping-list items

Revision ID: i5d0e1f2a3b4
Revises: h4c9d0e1f2a3
Create Date: 2026-07-29

"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "i5d0e1f2a3b4"
down_revision: str | Sequence[str] | None = "h4c9d0e1f2a3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "shopping_list_items",
        sa.Column("image_url", sa.Text(), nullable=True),
    )
    op.execute(
        """
        UPDATE shopping_list_items AS list_item
        SET image_url = product.image_url
        FROM products AS product
        WHERE list_item.product_id = product.id
        """
    )
    op.drop_column("products", "image_url")


def downgrade() -> None:
    op.add_column(
        "products",
        sa.Column("image_url", sa.Text(), nullable=True),
    )
    op.drop_column("shopping_list_items", "image_url")
