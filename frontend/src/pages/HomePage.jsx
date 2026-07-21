import { useState } from "react";
import ProductSearch from "../components/ProductSearch";
import ShoppingList from "../components/ShoppingList";
import ListSelector from "../components/ListSelector";
import Header from "../components/Header";
import Box from "@mui/material/Box";

function HomePage() {
  const [selectedProducts, setSelectedProducts] = useState([]);

  function addProduct(product) {
    setSelectedProducts((currentProducts) => {
      const alreadyAdded = currentProducts.some(
        (currentProduct) => currentProduct.id === product.id,
      );

      if (alreadyAdded) {
        return currentProducts;
      }

      return [...currentProducts, product];
    });
  }

  return (
    <>
      <Header />
      <Box
        component="main"
        sx={{
          display: "grid",
          gap: 4,
          p: 2,
        }}
      > 
        <ListSelector />
        <ProductSearch onAddProduct={addProduct} />
        <ShoppingList products={selectedProducts} />
      </Box>
    </>
    
  );
}

export default HomePage;
