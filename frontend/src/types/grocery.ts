export type GroceryEstimateRequest = {
  store: string;
  zip_code: string;
  items_text: string;
};

export type EstimatedItem = {
  name: string;
  quantity: number;
  unit: string;
  unit_price: number | null;
  total_price: number | null;
  found: boolean;
};

export type GroceryEstimateResponse = {
  store: string;
  zip_code: string;
  estimated_total: number;
  items_found: number;
  items_not_found: number;
  total_items: number;
  items: EstimatedItem[];
};
