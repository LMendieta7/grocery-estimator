import {
  BarChart3,
  ChevronDown,
  History,
  ListChecks,
  Settings,
  ShoppingBasket,
  Store
} from "lucide-react";

const navigation = [
  { label: "Estimate List", icon: ListChecks, active: true },
  { label: "Saved Lists", icon: ShoppingBasket },
  { label: "Frequent Items", icon: BarChart3 },
  { label: "Price History", icon: History },
  { label: "Stores", icon: Store },
  { label: "Settings", icon: Settings }
];

export function Sidebar() {
  return (
    <aside className="flex min-h-screen w-64 flex-col border-r border-slate-200 bg-white px-5 py-6">
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-accent-600 text-white">
          <ShoppingBasket className="h-5 w-5" />
        </div>
        <div>
          <p className="text-base font-semibold text-slate-950">Grocery Estimator</p>
        </div>
      </div>

      <nav className="mt-9 space-y-2">
        {navigation.map((item) => (
          <button
            key={item.label}
            className={`flex w-full items-center gap-3 rounded-lg px-3 py-3 text-left text-sm font-medium ${
              item.active
                ? "bg-accent-50 text-accent-700"
                : "text-slate-600 hover:bg-slate-50 hover:text-slate-950"
            }`}
          >
            <item.icon className="h-4 w-4" />
            {item.label}
          </button>
        ))}
      </nav>

      <div className="mt-auto border-t border-slate-200 pt-4">
        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-full bg-accent-100 text-sm font-semibold text-accent-700">
            L
          </div>
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-semibold text-slate-950">Leonardo</p>
            <p className="truncate text-xs text-slate-500">leo@example.com</p>
            <span className="mt-1 inline-flex rounded-full bg-accent-100 px-2 py-0.5 text-xs font-medium text-accent-700">
              Premium Plan
            </span>
          </div>
          <ChevronDown className="h-4 w-4 text-slate-400" />
        </div>
      </div>
    </aside>
  );
}
