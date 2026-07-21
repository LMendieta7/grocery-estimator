import { getAllShoppingLists } from "../services/shoppingListApi";
import { useEffect, useState } from "react";

import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import AddIcon from "@mui/icons-material/Add";



function ListSelector({ onAddList }){
    const [shoppingLists, setShoppingLists] = useState([]);
    const [selectedListId, setSelectedListId] = useState("");

    function handleListChange(event) {
        const newListId = event.target.value;
        setSelectedListId(newListId);
    }
        useEffect(() => {
        async function loadShoppingLists() {
            const lists = await getAllShoppingLists();

            setShoppingLists(lists);
            if (lists.length > 0) {
                setSelectedListId(lists[0].id);
            }
            
        }

        loadShoppingLists();
    }, []);
    return (
        <Box sx={{ display: "flex", alignItems: "center", gap: 1 }}>
            <FormControl size="small" sx={{ minWidth: 200 }}>
                <InputLabel id="shopping-list-label">
                    Shopping List
                </InputLabel>
                <Select
                    labelId="shopping-list-label"
                    label="Shopping list"
                    value={selectedListId}
                    onChange={handleListChange}
                >
                {shoppingLists.map((list) => (
                    <MenuItem key={list.id} value={list.id}>
                        {list.name}
                    </MenuItem>
                ))}
                </Select>
            </FormControl>

            <Button
                variant="outlined"
                size="small"
                startIcon={<AddIcon />}
                onClick={onAddList}
            >
                New list
            </Button>
        </Box>
    );
}

export default ListSelector;
