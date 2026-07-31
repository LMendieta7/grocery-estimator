
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "/api";


export async function getAllCategories() {
  const response = await fetch(
    `${API_BASE_URL}/categories`
    );

  if (!response.ok) {
    throw new Error("Could not get categories");
  }

  return response.json();
}