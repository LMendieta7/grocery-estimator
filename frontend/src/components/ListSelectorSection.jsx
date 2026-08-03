import { getAllShoppingLists } from "../services/shoppingListApi";
import { useEffect, useState } from "react";

import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";



function ListSelectorSection({ selectedListId, onSelectList, totalItemsCount, checkedCount}){
    const [shoppingLists, setShoppingLists] = useState([]);

    function handleListChange(event) {
        const newListId = event.target.value;
        onSelectList(newListId);
    }
        useEffect(() => {
        async function loadShoppingLists() {
            const lists = await getAllShoppingLists();

            setShoppingLists(lists);
            if (lists.length > 0) {
                onSelectList(lists[0].id);
            }
            
        }

        loadShoppingLists();
    }, [onSelectList]);
    
    return (
        <Box sx={{ display: "flex", alignItems: "flex-end", gap: 10 }}>
            <FormControl size="small" sx={{ minWidth: 250 }}>
                <FormLabel id="shopping-list-label" sx={{ mb: 0.75 }}>
                    Shopping List
                </FormLabel>
                <Select
                    labelId="shopping-list-label"
                    value={selectedListId}
                    onChange={handleListChange}
                >
                {shoppingLists.map((list) => (
                    <MenuItem key={list.id} value={list.id}>
                        {list.name}  {`(${checkedCount}/${totalItemsCount})`}
                    </MenuItem>
                ))}
                </Select>
                
            </FormControl>

            <Button variant="contained" sx={{alignItems: "center"}}>
                add
            </Button>

        </Box>
    );
}

export default ListSelectorSection;
