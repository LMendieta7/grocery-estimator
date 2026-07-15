import { useState } from "react";
import "./App.css";

const API_BASE_URL = "http://localhost:8000/api";

function App() {
  const [groceryText, setGroceryText] = useState("");
  const [store, setStore] = useState("");
  const [prices, setPrices] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  async function searchPrices() {
    setIsLoading(true);
    setError("");

    try {
      const response = await fetch(`${API_BASE_URL}/products/bulk/prices`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          product: groceryText,
          store: store || null,
        }),
      });

      if (!response.ok) {
        throw new Error("Could not load prices. Check the backend response.");
      }

      const data = await response.json();
      setPrices(data);
    } catch (requestError) {
      setPrices([]);
      setError(requestError.message);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="app-shell">
      <section className="search-panel">
        <div className="heading-group">
          <p className="eyebrow">Smart Grocery</p>
          <h1>Compare grocery prices</h1>
        </div>

        <div className="form-grid">
          <label className="field">
            <span>Grocery list</span>
            <textarea
              value={groceryText}
              onChange={(event) => setGroceryText(event.target.value)}
              placeholder={"milk\nbread\neggs"}
              rows={8}
            />
          </label>

          <label className="field">
            <span>Store</span>
            <input
              value={store}
              onChange={(event) => setStore(event.target.value)}
              placeholder="Optional store"
            />
          </label>

          <button type="button" onClick={searchPrices} disabled={isLoading}>
            {isLoading ? "Searching..." : "Search prices"}
          </button>
        </div>

        {error && <p className="error-message">{error}</p>}
      </section>

      <section className="results-section">
        <div className="results-header">
          <h2>Results</h2>
          <span>{prices.length} prices found</span>
        </div>

        {prices.length === 0 ? (
          <p className="empty-state">Search for items to see prices here.</p>
        ) : (
          <table>
            <thead>
              <tr>
                <th>Product</th>
                <th>Brand</th>
                <th>Size</th>
                <th>Store</th>
                <th>Price</th>
              </tr>
            </thead>
            <tbody>
              {prices.map((item) => (
                <tr key={`${item.product_id}-${item.store_id}`}>
                  <td>{item.product_name}</td>
                  <td>{item.brand || "Unknown"}</td>
                  <td>{item.size || "Unknown"}</td>
                  <td>{item.store_name}</td>
                  <td>${Number(item.price).toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </main>
  );
}

export default App;
