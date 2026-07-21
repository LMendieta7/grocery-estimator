
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "/api";

export async function searchProducts(searchText, signal) {
  const response = await fetch(
    `${API_BASE_URL}/products/search?q=${encodeURIComponent(searchText)}`,
    { signal },
  );

  if (!response.ok) {
    throw new Error("Could not search product");
  }

  return response.json();
}
