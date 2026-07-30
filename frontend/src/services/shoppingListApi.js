
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "/api";


export async function getAllShoppingLists() {
  const response = await fetch(
    `${API_BASE_URL}/shopping-lists`
    );

  if (!response.ok) {
    throw new Error("Could not get lists");
  }

  return response.json();
}


export async function getShoppingListDetail(shoppingListId) {
  const response = await fetch(
    `${API_BASE_URL}/shopping-lists/${shoppingListId}`,
  );

  if (!response.ok) {
    throw new Error("Could not get shopping list details");
  }

  return response.json();
}

export async function addProductToShoppingList(shoppingListId, item) {
  const response = await fetch(
    `${API_BASE_URL}/shopping-lists/${shoppingListId}/items`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(item),
    },
  );

  if (!response.ok) {
    throw new Error("Could not add product to shopping list");
  }

  return response.json();
}

export async function deleteShoppingListItem(shoppingListId, itemId) {
  const response = await fetch(
    `${API_BASE_URL}/shopping-lists/${shoppingListId}/items/${itemId}`,
    {
      method: "DELETE",
    },
  );

  if (!response.ok) {
    throw new Error("Could not delete shopping list item");
  }

  return response.json();
}
