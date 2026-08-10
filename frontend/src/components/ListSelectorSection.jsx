import { getAllShoppingLists } from "../services/shoppingListApi";
import { addShoppingList } from "../services/shoppingListApi";
import { useEffect, useState } from "react";

import FormControl from "@mui/material/FormControl";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import Box from "@mui/material/Box";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";

import ListDialog from "./ListDialog";


function ListSelectorSection({ selectedListId, onSelectList}){
    const [shoppingLists, setShoppingLists] = useState([]);
    const [listDialogOpen, setListDialogOpen] = useState(false);

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
    
    function handleDialogClickOpen(){
        setListDialogOpen(true);
    }

    function handleDialogClose(){
        setListDialogOpen(false);
    }

    async function createShoppingList(request) {
        
        const newList = await addShoppingList(request);
    
        setShoppingLists((currentLists) => [
        ...currentLists,
        newList,
    ]);

    }
    
        
     

    return (
        <Box
            sx={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                gap: 3,
                width: "100%",
                
            }}
        >
            <FormControl size="small" sx={{ width: {
                                                xs: "calc(100% - 52px)",
                                                sm: "40%",
                                            },
                                            minWidth: 0,
                                            "& .MuiOutlinedInput-root": { 
                                                borderRadius: "8px",
                                                "& .MuiOutlinedInput-notchedOutline": {
                                                    borderColor: "#c9d0cb",
                                                },
                                                "&:hover .MuiOutlinedInput-notchedOutline": {
                                                    borderColor: "darkgreen",
                                                },
                                                "&.Mui-focused .MuiOutlinedInput-notchedOutline": {
                                                    borderColor: "darkgreen",
                                                },
                                            },
                                        }}
            >
                <Select
                    labelId="shopping-list-label"
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
            
            <Fab
                size="small"
                onClick={handleDialogClickOpen}
                aria-label="Add shopping list"
                sx={{
                    flexShrink: 0,
                    bgcolor: "#0B5D1E",
                    color: "#FFF",
                    boxShadow: "0 4px 12px rgba(0,0,0,0.18)",
                    "&:hover": {
                        bgcolor: "#094A18",
                    },
                }}
            >
                <AddIcon sx={{ fontSize: 25 }} />
            </Fab>
            {listDialogOpen && (
                <ListDialog
                    onClose={handleDialogClose}
                    onCreate={createShoppingList}
                />        
            )}
        
        </Box>
    );
}

export default ListSelectorSection;
