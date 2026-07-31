from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from backend.app.categories.models import CategoryTable
from backend.app.categories.services import CategoryService


def test_get_all_categories():
    # Arrange
    category_one = CategoryTable(id=1, name="Produce")
    category_two = CategoryTable(id=2, name="Dairy")

    db = MagicMock(spec=Session)
    db.scalars.return_value.all.return_value = [
        category_one,
        category_two,
    ]

    service = CategoryService(db)

    # Act
    result = service.get_all_categories()

    # Assert
    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].name == "Produce"

    assert result[1].id == 2
    assert result[1].name == "Dairy"

    db.scalars.assert_called_once()
