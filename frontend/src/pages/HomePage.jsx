import { useCallback, useState, useEffect } from "react";
import ProductSearch from "../components/ProductSearch";
import ShoppingList from "../components/ShoppingList";
import ListSelector from "../components/ListSelector";
import SummaryBar from "../components/SummaryBar";
import Header from "../components/Header";
import Box from "@mui/material/Box";

import {
  addProductToShoppingList,
  deleteShoppingListItem,
  getShoppingListDetail,
} from "../services/shoppingListApi";



function HomePage() {
  const [selectedListId, setSelectedListId] = useState("");
  const [shoppingListDetail, setShoppingListDetail] = useState(null);

  useEffect(() => {
    async function loadShoppingListDetails() {
      if (!selectedListId) {
        return;
      }

      try {
        const listDetails = await getShoppingListDetail(selectedListId);
        setShoppingListDetail(listDetails);
  
      } catch (error) {
        console.error("Failed to load shopping list details:", error);
      }
    }

    loadShoppingListDetails();
  }, [selectedListId]);

  async function addProductToList(product) {
    if (!selectedListId) {
      return;
    }


    const itemRequest = {
      product_id: product.id,
      quantity: 1,
    };

    const updateDetail = await addProductToShoppingList(selectedListId, itemRequest);

    setShoppingListDetail(updateDetail);

    }

  const handleListSelect = useCallback((listId) => {
    setSelectedListId(listId);
    
  }, []);

  async function deleteItemFromList(itemId) {
    if (!selectedListId) {
        return;
      }
    const updateDetail = await deleteShoppingListItem(selectedListId, itemId);
    setShoppingListDetail(updateDetail);
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
        <ListSelector 
          onSelectList={handleListSelect}
          selectedListId={selectedListId}

        />
        <ProductSearch onAddProductToList={addProductToList} />
        
        {shoppingListDetail && (
        <>
          <SummaryBar shoppingListDetail={shoppingListDetail} />
          <ShoppingList
            items={shoppingListDetail.items}
            onDeleteItem={deleteItemFromList}
          />
        </>
      )}
      </Box>
    </>
    
  );
}

export default HomePage;
