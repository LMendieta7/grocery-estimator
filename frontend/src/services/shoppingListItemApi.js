const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "/api";

export async function addProductToShoppingList(shopping_list_id, product){
    const response = await fetch(`${API_BASE_URL}/shopping-lists/${shopping_list_id}/items`, {
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

