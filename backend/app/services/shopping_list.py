from backend.app.schemas.shopping_list import GetAllListResponse

class ShoppingListService:
    def __init__(self, db, shopping_list_repository):
        self.db = db
        self.shopping_list_repository=shopping_list_repository

    
    def get_all_lists(self):
        rows = self.shopping_list_repository.get_all_lists()

        if rows is None:
            return None
        
        return [GetAllListResponse(
            id=row.id,
            name=row.name,
            created_at=row.created_at,
        )
        for row in rows
        ]