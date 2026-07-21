
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
