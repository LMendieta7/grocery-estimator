import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import Box from "@mui/material/Box";
import Checkbox from "@mui/material/Checkbox";


function ShoppingList({ products }) {

    return (
        <Box component="section">            
            <List>
                {products.map((product) => (
                    <ListItem key={product.id} divider>
                        <Box sx={{ display: "flex", alignItems: "center", width: "100%", gap: 2 }}>
                            <Checkbox
                                checked={true}
                            />
                            <ListItemText
                                primary={product.name}
                                secondary={`$${product.estimated_price}`}
                            />
                        </Box>
                    </ListItem>
                ))}
            </List>
        </Box>

    );
}

export default ShoppingList;
