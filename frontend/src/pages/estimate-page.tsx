import {
  Bell,
  Calculator,
  Download,
  FileText,
  Lightbulb,
  MapPin,
  Moon,
  Pencil,
  Store,
  Sun,
  Tag,
  Trash2
} from "lucide-react";
import { FormEvent, useMemo, useState } from "react";

import { Sidebar } from "../components/layout/sidebar";
import { StatusBadge } from "../components/ui/badge";
import { Button } from "../components/ui/button";
import { Card } from "../components/ui/card";
import { estimateGroceryList } from "../lib/api";
import { formatCurrency } from "../lib/format";
import type { GroceryEstimateResponse } from "../types/grocery";

const defaultText =
  "2 gallons milk\n1 dozen eggs\n1 loaf white bread\n3 lb chicken breast\n2 bananas\n3 tomatoes";
const stores = ["Walmart", "Target", "Kroger"];
const recentLists = [
  { date: "June 14, 2025 -- 6:01 PM", items: 6, total: 25.05 },
  { date: "June 12, 2025 -- 4:33 PM", items: 5, total: 18.2 },
  { date: "June 10, 2025 -- 7:15 PM", items: 6, total: 24.1 },
  { date: "June 8, 2025 -- 1:20 PM", items: 8, total: 41.32 },
  { date: "June 6, 2025 -- 11:02 AM", items: 4, total: 12.45 }
];

export function EstimatePage() {
  const [store, setStore] = useState("Walmart");
  const [zipCode, setZipCode] = useState("17601");
  const [itemsText, setItemsText] = useState(defaultText);
  const [estimate, setEstimate] = useState<GroceryEstimateResponse | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  const missingItems = useMemo(
    () => estimate?.items.filter((item) => !item.found) ?? [],
    [estimate]
  );
  const inputItemCount = useMemo(
    () => itemsText.split("\n").filter((line) => line.trim()).length,
    [itemsText]
  );

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError("");

    try {
      const result = await estimateGroceryList({
        store,
        zip_code: zipCode,
        items_text: itemsText
      });
      setEstimate(result);
    } catch (requestError) {
      setError(
        requestError instanceof Error
          ? requestError.message
          : "Unable to estimate grocery list"
      );
    } finally {
      setLoading(false);
    }
  }

  function handleClear() {
    setItemsText("");
    setEstimate(null);
    setError("");
  }

  return (
    <div className="flex min-h-screen bg-slate-50">
      <Sidebar />
      <main className="flex min-w-0 flex-1 flex-col">
        <header className="flex h-20 items-center justify-between border-b border-slate-200 bg-white px-8">
          <div>
            <h1 className="text-2xl font-semibold tracking-tight text-slate-950">
              Estimate Your Grocery List
            </h1>
            <p className="mt-1 text-sm text-slate-500">
              Add your items, choose a store, and see an estimated total.
            </p>
          </div>
          <div className="flex items-center gap-3">
            <div className="flex h-10 items-center gap-2 rounded-lg border border-slate-200 bg-white px-3">
              <Store className="h-4 w-4 text-slate-500" />
              <span className="text-sm font-semibold text-slate-700">Store:</span>
            <select
                className="bg-transparent text-sm font-medium text-slate-700 outline-none"
              value={store}
              onChange={(event) => setStore(event.target.value)}
            >
              {stores.map((storeName) => (
                <option key={storeName}>{storeName}</option>
              ))}
            </select>
            </div>
            <label className="flex h-10 items-center gap-2 rounded-lg border border-slate-200 bg-white px-3">
              <MapPin className="h-4 w-4 text-slate-500" />
              <span className="text-xs font-medium text-slate-500">Zip Code:</span>
              <input
                className="w-16 bg-transparent text-sm font-medium text-slate-700 outline-none"
                value={zipCode}
                onChange={(event) => setZipCode(event.target.value)}
                placeholder="17601"
              />
            </label>
            <button
              className="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white text-slate-600"
              onClick={() => setDarkMode((value) => !value)}
              aria-label="Toggle theme"
            >
              {darkMode ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
            </button>
            <button
              className="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white text-slate-600"
              aria-label="Notifications"
            >
              <Bell className="h-4 w-4" />
            </button>
          </div>
        </header>

        <div className="grid flex-1 grid-cols-[minmax(0,1fr)_390px] gap-4 p-6">
          <div className="space-y-6">
            <Card className="p-6">
              <div className="mb-3 flex items-start justify-between">
                <div>
                  <h2 className="text-lg font-semibold text-slate-950">Add Items</h2>
                  <p className="mt-1 text-sm text-slate-500">
                    Type or paste your grocery list (one item per line)
                  </p>
                </div>
                <p className="text-sm font-medium text-accent-700">
                  Tips: You can include quantity and unit
                </p>
              </div>

              <form onSubmit={handleSubmit}>
                <div className="relative">
                  <textarea
                    className="min-h-44 w-full resize-y rounded-lg border border-accent-600 bg-white p-4 text-sm leading-6 text-slate-800 outline-none transition placeholder:text-slate-400 focus:ring-4 focus:ring-accent-100"
                    value={itemsText}
                    onChange={(event) => setItemsText(event.target.value)}
                    placeholder={"2 gallons milk\n1 dozen eggs\n1 loaf bread\n3 lb chicken breast"}
                  />
                  <span className="absolute bottom-3 right-3 text-xs font-medium text-slate-500">
                    {inputItemCount} items
                  </span>
                </div>

                {error && (
                  <p className="mt-3 rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700">
                    {error}
                  </p>
                )}

                <div className="mt-4 flex gap-3">
                  <Button type="submit" disabled={loading || !itemsText.trim()}>
                    <Calculator className="mr-2 h-4 w-4" />
                    {loading ? "Estimating..." : "Estimate Total"}
                  </Button>
                  <Button type="button" variant="secondary" onClick={handleClear}>
                    <Trash2 className="mr-2 h-4 w-4" />
                    Clear List
                  </Button>
                </div>
              </form>
            </Card>

            <Card className="overflow-hidden">
              <div className="border-b border-slate-200 px-6 py-5">
                <h2 className="text-lg font-semibold text-slate-950">Estimated Items</h2>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full text-left text-sm">
                  <thead className="bg-white text-xs text-slate-500">
                    <tr>
                      <th className="px-6 py-3 font-semibold">Item</th>
                      <th className="px-6 py-3 font-semibold">Qty</th>
                      <th className="px-6 py-3 font-semibold">Unit</th>
                      <th className="px-6 py-3 font-semibold">Unit Price</th>
                      <th className="px-6 py-3 font-semibold">Total</th>
                      <th className="px-6 py-3 font-semibold">Status</th>
                      <th className="px-6 py-3 font-semibold"></th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {(estimate?.items ?? []).map((item, index) => (
                      <tr key={`${item.name}-${index}`} className="bg-white">
                        <td className="px-6 py-4 font-semibold text-slate-950">
                          <span className="mr-3 text-lg">{itemIcon(item.name)}</span>
                          {item.name}
                        </td>
                        <td className="px-6 py-4 text-slate-600">{item.quantity}</td>
                        <td className="px-6 py-4 text-slate-600">{item.unit}</td>
                        <td className="px-6 py-4 font-semibold text-slate-950">
                          {formatCurrency(item.unit_price)}
                        </td>
                        <td className="px-6 py-4 font-semibold text-slate-950">
                          {formatCurrency(item.total_price)}
                        </td>
                        <td className="px-6 py-4">
                          <StatusBadge found={item.found} />
                        </td>
                        <td className="px-6 py-4">
                          {item.found && (
                            <button className="flex h-8 w-8 items-center justify-center rounded-lg border border-slate-200 text-slate-500">
                              <Pencil className="h-4 w-4" />
                            </button>
                          )}
                        </td>
                      </tr>
                    ))}
                    {!estimate && (
                      <tr>
                        <td className="px-6 py-12 text-center text-slate-500" colSpan={7}>
                          Run an estimate to see item-level pricing.
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </div>
              <div className="flex items-center justify-between border-t border-slate-100 px-6 py-4">
                <p className="text-xs text-slate-500">Prices may vary by store and location.</p>
                <Button type="button" variant="secondary" className="h-9">
                  <Download className="mr-2 h-4 w-4" />
                  Export as CSV
                </Button>
              </div>
            </Card>
          </div>

          <aside className="space-y-4">
            <Card className="p-6">
              <h2 className="text-lg font-semibold text-slate-950">Estimated Total</h2>
              <p className="mt-3 text-center text-4xl font-bold tracking-tight text-accent-700">
                {formatCurrency(estimate?.estimated_total ?? 0)}
              </p>
              <div className="mt-5 rounded-lg border border-slate-200">
                <SummaryRow label="Items found" value={estimate?.items_found ?? 0} />
                <SummaryRow
                  label="Items not found"
                  value={estimate?.items_not_found ?? 0}
                  danger
                />
                <SummaryRow label="Total items" value={estimate?.total_items ?? 0} />
              </div>
              <div className="mt-4 flex gap-3 rounded-lg border border-accent-100 bg-accent-50 p-4 text-sm font-medium text-accent-700">
                <Tag className="mt-0.5 h-4 w-4 shrink-0" />
                <p>Prices are based on current average from {store} in {zipCode}.</p>
              </div>
            </Card>

            <Card className="p-6">
              <div className="flex items-center justify-between">
                <h2 className="text-lg font-semibold text-slate-950">Recent Lists</h2>
                <Button type="button" variant="secondary" className="h-8 px-3">
                  View All
                </Button>
              </div>
              <div className="mt-4 divide-y divide-slate-100">
                {recentLists.map((list) => (
                  <div key={list.date} className="flex items-center gap-3 py-3">
                    <FileText className="h-5 w-5 text-slate-500" />
                    <div className="min-w-0 flex-1">
                      <p className="truncate text-sm font-medium text-slate-700">{list.date}</p>
                      <p className="text-xs text-slate-500">{list.items} items</p>
                    </div>
                    <p className="text-sm font-semibold text-accent-700">
                      {formatCurrency(list.total)}
                    </p>
                  </div>
                ))}
              </div>
            </Card>

            <Card className="p-6">
              <div className="flex items-center gap-2">
                <Lightbulb className="h-4 w-4 text-slate-700" />
                <h2 className="text-lg font-semibold text-slate-950">Quick Tips</h2>
              </div>
              <ul className="mt-4 space-y-2 text-sm text-slate-600">
                <li className="text-accent-700">✓ Include quantity and unit for more accurate results.</li>
                <li className="text-accent-700">✓ Examples: 2 milk, 1 dozen eggs, 3 lb chicken</li>
                <li className="text-accent-700">✓ You can edit quantities after estimating.</li>
              </ul>
            </Card>

            {missingItems.length > 0 && (
              <Card className="p-6">
                <h2 className="text-base font-semibold text-slate-950">Missing Items</h2>
                <div className="mt-4 flex flex-wrap gap-2">
                  {missingItems.map((item, index) => (
                    <span
                      key={`${item.name}-${index}`}
                      className="rounded-full bg-red-50 px-3 py-1 text-xs font-medium text-red-700"
                    >
                      {item.name}
                    </span>
                  ))}
                </div>
              </Card>
            )}
          </aside>
        </div>
      </main>
    </div>
  );
}

function SummaryRow({
  label,
  value,
  danger = false
}: {
  label: string;
  value: number;
  danger?: boolean;
}) {
  return (
    <div className="flex items-center justify-between border-b border-slate-100 px-4 py-3 last:border-b-0">
      <span className="text-sm font-medium text-slate-600">{label}</span>
      <span className={`text-sm font-semibold ${danger ? "text-red-600" : "text-slate-950"}`}>
        {value}
      </span>
    </div>
  );
}

function itemIcon(name: string): string {
  const normalized = name.toLowerCase();
  if (normalized.includes("milk")) return "🥛";
  if (normalized.includes("egg")) return "🥚";
  if (normalized.includes("bread")) return "🍞";
  if (normalized.includes("chicken")) return "🍗";
  if (normalized.includes("banana")) return "🍌";
  if (normalized.includes("tomato")) return "🍅";
  return "🛒";
}
