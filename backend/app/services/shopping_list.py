from backend.app.schemas.shopping_list import GetAllListResponse, ShoppingListDetailResponse
from backend.app.schemas.shopping_list_item import ShoppingListItemResponse
from decimal import Decimal

class ShoppingListService:
    def __init__(self, db, shopping_list_repository, shopping_list_item_repository):
        self.db = db
        self.shopping_list_repository=shopping_list_repository
        self.shopping_list_item_repository=shopping_list_item_repository
        
    
    def get_all_lists(self):
        rows = self.shopping_list_repository.get_all_lists()

        return [GetAllListResponse(
            id=row.id,
            name=row.name,
            created_at=row.created_at,
        )
        for row in rows
        ]
    
    def get_list_detail(self, shopping_list_id):
        shopping_list = self.shopping_list_repository.get_by_id(shopping_list_id)

        if shopping_list is None:
            return None
        
        list_items_with_products = (self.shopping_list_item_repository
                           .get_items_with_product_details(shopping_list_id)
                           )
        
        items = []
        estimated_total = Decimal("0.00")
        checked_count = 0

        for list_item, product, category in list_items_with_products:
            
            if list_item.is_checked:
                checked_count += 1
            estimated_total += list_item.quantity * product.estimated_price

            items.append(ShoppingListItemResponse(
                        id=list_item.id,
                        shopping_list_id=list_item.shopping_list_id,
                        product_id=list_item.product_id,
                        product_name_snapshot=list_item.product_name_snapshot,
                        category=category.name,
                        quantity=list_item.quantity,
                        estimated_price=product.estimated_price,
                        notes=list_item.notes,
                        is_checked=list_item.is_checked,
                    )
            )
        total_count =len(items)
                
        response = ShoppingListDetailResponse(
            id=shopping_list.id,
            name=shopping_list.name,
            items=items,
            checked_count=checked_count,
            total_count=total_count,
            estimated_total=estimated_total,
        ) 
            
        return response
