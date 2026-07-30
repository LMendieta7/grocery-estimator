import { useState } from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import Box from "@mui/material/Box";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import useMediaQuery from "@mui/material/useMediaQuery";
import { useTheme } from "@mui/material/styles";


const inputStyles = {
    "& .MuiOutlinedInput-root": {
        bgcolor: "white",
    },
};

const wholeQuantityUnits = new Set(["each", "pack", "dozen"]);


function EditItemDialog({onClose, item, onDeleteItem}) {

    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

    const [productName, setProductName] = useState(item.product_name ?? "");
    const [category, setCategory] = useState(item.category);
    const [quantity, setQuantity] = useState(Number(item.quantity));
    const [unit, setUnit] = useState(item.unit ?? "each");
    const [estimatedPrice, setEstimatedPrice] = useState(
        item.estimated_price ?? "",
    );
    const [notes, setNotes] = useState(item.notes ?? "");

    const quantityStep = wholeQuantityUnits.has(unit) ? 1 : 0.25;

    function decreaseQuantity() {
        setQuantity((currentQuantity) => (
            Math.max(
                quantityStep,
                Number((currentQuantity - quantityStep).toFixed(2)),
            )
        ));
    }

    function increaseQuantity() {
        setQuantity((currentQuantity) => (
            Number((currentQuantity + quantityStep).toFixed(2))
        ));
    }

    function handleSubmit(event) {
        event.preventDefault();
    }
    async function handleDelete() {
        await onDeleteItem(item.id);
        onClose();
    }

    return (

        <Dialog
            open
            onClose={onClose}
            fullScreen={isMobile}
            fullWidth
            maxWidth="xs"
            slotProps={{
                paper: {
                    sx: {
                        bgcolor: "var(--app-background)",
                    },
                },
            }}
        >
            <DialogTitle align="center">Edit {item.product_name} </DialogTitle>
            <Box component="form" onSubmit={handleSubmit}>
            <DialogContent>
            
            <TextField
                label="Item Name"
                value={productName}
                onChange={(event) => setProductName(event.target.value)}
                fullWidth
                margin="normal"
                sx={inputStyles}
            />
            <TextField
                label="Category"
                value={category}
                onChange={(event) => setCategory(event.target.value)}
                fullWidth
                margin="normal"
                sx={inputStyles}
            />
            <Typography variant="body2" color="text.secondary" sx={{ mt: 2 }}>
                Quantity
            </Typography>
            <Box
                sx={{
                    display: "inline-flex",
                    border: 1,
                    borderColor: "divider",
                    borderRadius: 1,
                    overflow: "hidden",
                    my: 1,
                }}
                alignItems="center"
            >
                <IconButton
                    aria-label="Decrease quantity"
                    onClick={decreaseQuantity}
                    disabled={quantity <= quantityStep}
                    sx={{
                        borderRadius: 0,
                        px: 1.5,
                        color: "primary.main",
                        bgcolor: "lightblue",
                        
                    }}
                >
                    <RemoveIcon />
                </IconButton>

                <Typography
                    aria-label={`Quantity: ${quantity}`}
                    sx={{
                        minWidth: 32,
                        textAlign: "center",
                        fontWeight: 600,
                        px: 2,
                        py: 1,
                        borderLeft: 1,
                        borderRight: 1,
                        borderColor: "divider",
                    }}
                >
                    {quantity}
                </Typography>

                <IconButton
                    aria-label="Increase quantity"
                    onClick={increaseQuantity}
                    sx={{
                        borderRadius: 0,
                        px: 1.5,
                        color: "primary.main",
                        bgcolor: "lightblue",
                    }}
                >
                    <AddIcon />
                </IconButton>
            </Box>
            <FormControl fullWidth margin="normal">
                <InputLabel id="item-unit-label">Unit</InputLabel>
                <Select
                    labelId="item-unit-label"
                    label="Unit"
                    value={unit}
                    onChange={(event) => setUnit(event.target.value)}
                    sx={{ bgcolor: "white" }}
                >
                    <MenuItem value="each">Each</MenuItem>
                    <MenuItem value="pack">Pack</MenuItem>
                    <MenuItem value="lb">Pound (lb)</MenuItem>
                    <MenuItem value="oz">Ounce (oz)</MenuItem>
                    <MenuItem value="kg">Kilogram (kg)</MenuItem>
                    <MenuItem value="g">Gram (g)</MenuItem>
                    <MenuItem value="L">Liter (L)</MenuItem>
                    <MenuItem value="mL">Milliliter (mL)</MenuItem>
                    <MenuItem value="gallon">Gallon</MenuItem>
                    <MenuItem value="dozen">Dozen</MenuItem>
                </Select>
            </FormControl>
            <TextField
                label="Estimated Price (optional)"
                type="number"
                value={estimatedPrice}
                onChange={(event) => setEstimatedPrice(event.target.value)}
                fullWidth
                margin="normal"
                sx={inputStyles}
                slotProps={{
                    htmlInput: {
                        min: 0,
                        step: "0.01",
                    },
                }}
            />
            <TextField
                label="Notes"
                value={notes}
                onChange={(event) => setNotes(event.target.value)}
                fullWidth
                multiline
                minRows={4}
                margin="normal"
                sx={inputStyles}
                
            />
            </DialogContent>

            <DialogActions sx={{ px: 3, pb: 2, bgcolor: "inherit" }}>

            <Button
                type="button"
                variant="contained"
                color="error"
                size="medium"
                sx={{ mr: "auto" }}
                onClick={handleDelete}
            >
                Delete
            </Button>
            <Button type="button" onClick={onClose} size="medium">
                Cancel
            </Button>

            <Button type="submit" variant="contained" size="medium">
                Save
            </Button>
            </DialogActions>
            </Box>
        </Dialog>
        
    );
}

export default EditItemDialog;
