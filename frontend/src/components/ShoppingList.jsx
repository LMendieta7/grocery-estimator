import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import Box from "@mui/material/Box";
import Checkbox from "@mui/material/Checkbox";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";

function ShoppingList({ items }) {
    return (
        <Box component="section">
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
                                gap: 2,
                            }}
                        >
                            <Checkbox
                                checked={item.is_checked}
                                sx={{ pl: 0, mt: 0.25 }}
                            />

                            <Box sx={{ flex: 1 }}>
                                <Typography sx={{ fontWeight: 600 }}>
                                    {item.product_name_snapshot}
                                </Typography>

                                <Typography
                                    variant="body2"
                                    color="text.secondary"
                                    sx={{ mt: 0.2, 
                                        overflow:"hidden",
                                        textOverflow:"ellipsis",
                                        whiteSpace:"nowrap",
                                        fontStyle:"italic"
                                    }}
                                >
                                    {item.quantity} &times;
                                    ${item.estimated_price}
                    
                                    {item.notes &&` •  ${item.notes}`}
                                </Typography>
                            </Box>
                        </Box>
                    </ListItem>
                ))}
            </List>
        </Box>
    );
}

export default ShoppingList;
