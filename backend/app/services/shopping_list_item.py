from backend.app.schemas.shopping_list_item import ShoppingListItemResponse
from backend.app.db.models.shopping_list_item import (
    ShoppingListItemTable,
)

class ShoppingListItemService:
    def __init__(
        self,
        db,
        shopping_list_repository,
        shopping_list_item_repository,
        product_repository,
    ):
        self.db = db
        self.shopping_list_repository = shopping_list_repository
        self.shopping_list_item_repository = shopping_list_item_repository
        self.product_repository = product_repository

    def add_item(self, shopping_list_id: int, request):
        shopping_list = self.shopping_list_repository.get_by_id(shopping_list_id)

        if shopping_list is None:
            return None
        
        product_with_category = self.product_repository.get_by_id_with_category(
            request.product_id
        )
        if product_with_category is None:
            return None

        product, category = product_with_category

        item = ShoppingListItemTable(
            shopping_list_id=shopping_list.id,
            product_id=product.id,
            product_name_snapshot=product.name,
            quantity=request.quantity,
            notes=request.notes,
            is_checked=False,
        )

        self.shopping_list_item_repository.create(item)
        self.db.commit()
        self.db.refresh(item)

        return ShoppingListItemResponse(
            id=item.id,
            shopping_list_id=item.shopping_list_id,
            product_id=item.product_id,
            product_name_snapshot=product.name,
            category=category.name,
            quantity=item.quantity,
            estimated_price=product.estimated_price,
            notes=item.notes,
            is_checked=item.is_checked,
        )
