const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "/api";

export async function addProductToShoppingList(shoppingListId, product){
    const response = await fetch(`${API_BASE_URL}/shopping-lists/${shoppingListId}/items`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(product),
    });

    if (!response.ok) {
        throw new Error("Failed to create product");
    }
    const data = await response.json();

    return data;
}

export async function deleteShoppingListItem(shoppingListId, itemId){
    const response = await fetch(`${API_BASE_URL}/shopping-lists/${shoppingListId}/items/${itemId}`,
    {
      method: "DELETE",
    }
    );

    if (!response.ok) {
        throw new Error("Could not delete item");
    }
    const data = await response.json();
    return data
}