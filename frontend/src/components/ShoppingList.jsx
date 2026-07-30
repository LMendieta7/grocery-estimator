import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import Box from "@mui/material/Box";
import Checkbox from "@mui/material/Checkbox";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import EditIcon from "@mui/icons-material/Edit";
import EditItemDialog from "./EditItemDialog";

import { useState } from "react";

function ShoppingList({ items, onDeleteItem }) {

    const [selectedItem, setSelectedItem] = useState(null);
   

    function handleClose() {
        setSelectedItem(null);
    }
    

    return (
        <Box
            component="section"
            sx={{
                minWidth: 0,
               
            }}
        >
            <List>
                {items.map((item) => (
                    <ListItem
                        key={item.id}
                        divider
                        alignItems="flex-start"
                        sx={{ pl: 0 }}
                    >
                        <Box
                            sx={{
                                display: "flex",
                                alignItems: "flex-start",
                                width: "100%",
                                minWidth: 0,
                                gap: 2,
                            }}
                        >
                            <Checkbox
                                checked={item.is_checked}
                                
                                size="small"
                                sx={{ pl: 0,
                                    mt: 0.25,
                                    // '& .MuiSvgIcon-root': { fontSize: 22 } 
                                }}
                            />

                            <Box sx={{ flex: 1, minWidth: 0 }}>
                                <Typography
                                    noWrap
                                    sx={{
                                        fontWeight: 600,    
                                    }}
                                >
                                    {item.product_name_snapshot}
                                </Typography>

                                <Typography
                                    noWrap
                                    variant="body2"
                                    color="text.secondary"
                                    sx={{ mt: 0.2,                                         
                                        fontStyle:"italic"
                                    }}
                                >
                                    {item.quantity} &times;
                                    ${item.estimated_price}
                    
                                    {item.notes &&` •  ${item.notes}`}
                                </Typography>
                              
                            </Box>
                                <IconButton
                                    aria-label={`Edit ${item.product_name_snapshot}`}
                                    onClick={()=> setSelectedItem(item)}
                                    size="small"
                                    color="primary"
                                    >
                                    <EditIcon fontSize="small" />
                                </IconButton>
                        </Box>
                    </ListItem>
                    
                ))}
            </List>
            { selectedItem && (
            <EditItemDialog
                onClose={handleClose}
                item={selectedItem}
                onDeleteItem={onDeleteItem}
            />
            )}
        </Box>
    );
}

export default ShoppingList;
