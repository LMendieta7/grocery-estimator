import { useState } from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import InputBase from "@mui/material/InputBase";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import IconButton from "@mui/material/IconButton";
import Box from "@mui/material/Box";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import useMediaQuery from "@mui/material/useMediaQuery";
import { useTheme } from "@mui/material/styles";

const wholeQuantityUnits = new Set(["each", "pack", "dozen"]);


function EditItemDialog({onClose, item, onDeleteItem, onUpdateListItem, categories}) {

    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

    const [productName, setProductName] = useState(item.product_name ?? "");
    const [categoryId, setCategoryId] = useState(Number(item.category_id));
    const [quantity, setQuantity] = useState(Number(item.quantity));
    const [unit, setUnit] = useState(item.unit ?? "each");
    const [estimatedPrice, setEstimatedPrice] = useState(
        item.estimated_price ?? "",
    );
    const [notes, setNotes] = useState(item.notes ?? "");

    const quantityStep = wholeQuantityUnits.has(unit) ? 1 : 0.25;

    function decreaseQuantity() {
        setQuantity((currentQuantity) => (
            Number(
                Math.max(
                    quantityStep,
                    Number(currentQuantity) - quantityStep,
                ).toFixed(2),
            )
        ));
    }

    function increaseQuantity() {
        setQuantity((currentQuantity) => (
            Number(
                (Number(currentQuantity || 0) + quantityStep).toFixed(2),
            )
        ));
    }

    function handleQuantityChange(event) {
        const nextQuantity = event.target.value;

        setQuantity(
            nextQuantity === "" ? "" : Number(nextQuantity),
        );
    }

    function handleUnitChange(event) {
        const nextUnit = event.target.value;
        setUnit(nextUnit);

        if (wholeQuantityUnits.has(nextUnit)) {
            setQuantity((currentQuantity) => (
                Math.max(1, Math.round(currentQuantity))
            ));
        }
    }

    async function handleSubmit(event) {
        event.preventDefault();
        const updates = {};

         if (productName !== item.product_name) {
            updates.name = productName;
        }

        if (unit !== item.unit) {
            updates.unit = unit;
        }
        if (categoryId !== item.category_id){
            updates.category_id = categoryId
        }

        if (Number(quantity) !== Number(item.quantity)) {
            updates.quantity = Number(quantity);
        }

        if (estimatedPrice !== (item.estimated_price ?? "")) {
            updates.estimated_price =
            estimatedPrice === "" ? null : Number(estimatedPrice);
        }

        if (notes !== (item.notes ?? "")) {
            updates.notes = notes;
        }

        if (Object.keys(updates).length === 0) {
            onClose();
            return;
        }

        await onUpdateListItem(item.id, updates);
        onClose();
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
            
            <FormControl fullWidth margin="normal">
                <FormLabel htmlFor="item-name" sx={{ mb: 0.75 }}>
                    Item Name
                </FormLabel>
                <TextField
                    id="item-name"
                    value={productName}
                    onChange={(event) => setProductName(event.target.value)}
                    fullWidth
                />
            </FormControl>
            <FormControl fullWidth size="small" margin="normal">
                <FormLabel id="category-label" sx={{ mb: 0.75 }}>
                    Category
                </FormLabel>
                <Select
                    labelId="category-label"
                    value={categoryId}
                    onChange={(event) => setCategoryId(event.target.value)}
                >
                    {categories.map((category) => (
                        <MenuItem key={category.id} value={category.id}>
                            {category.name}
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
            <FormControl component="fieldset" margin="normal">
                <FormLabel component="legend" sx={{ mb: 0.75 }}>
                    Quantity
                </FormLabel>
                <Box
                    sx={{
                        display: "inline-flex",
                        border: 1,
                        borderColor: "divider",
                        borderRadius: 1,
                        overflow: "hidden",
                    }}
                    alignItems="center"
                >
                    <IconButton
                        aria-label="Decrease quantity"
                        onClick={decreaseQuantity}
                        disabled={
                            quantity === ""
                            || Number(quantity) <= quantityStep
                        }
                        sx={{
                            borderRadius: 0,
                            px: 1.5,
                            color: "primary.main",
                            bgcolor: "lightblue",
                        }}
                    >
                        <RemoveIcon />
                    </IconButton>

                    <InputBase
                        type="number"
                        value={quantity}
                        onChange={handleQuantityChange}
                        sx={{
                            width: 70,
                            fontWeight: 600,
                            bgcolor: "white",
                            borderLeft: 1,
                            borderRight: 1,
                            borderColor: "divider",
                            "& input": {
                                textAlign: "center",
                                py: 1,
                                MozAppearance: "textfield",
                            },
                            "& input::-webkit-outer-spin-button, & input::-webkit-inner-spin-button": {
                                WebkitAppearance: "none",
                                margin: 0,
                            },
                        }}
                        slotProps={{
                            input: {
                                "aria-label": "Quantity",
                                min: quantityStep,
                                step: quantityStep,
                                required: true,
                            },
                        }}
                    />

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
            </FormControl>
            <FormControl fullWidth margin="normal">
                <FormLabel id="item-unit-label" sx={{ mb: 0.75 }}>
                    Unit
                </FormLabel>
                <Select
                    labelId="item-unit-label"
                    value={unit}
                    onChange={handleUnitChange}
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
            <FormControl fullWidth margin="normal">
                <FormLabel htmlFor="estimated-price" sx={{ mb: 0.75 }}>
                    Estimated Price (optional)
                </FormLabel>
                <TextField
                    id="estimated-price"
                    type="number"
                    value={estimatedPrice}
                    onChange={(event) => setEstimatedPrice(event.target.value)}
                    fullWidth
                    slotProps={{
                        htmlInput: {
                            min: 0,
                            step: "0.01",
                        },
                    }}
                />
            </FormControl>
            <FormControl fullWidth margin="normal">
                <FormLabel htmlFor="item-notes" sx={{ mb: 0.75 }}>
                    Notes
                </FormLabel>
                <TextField
                    id="item-notes"
                    value={notes}
                    onChange={(event) => setNotes(event.target.value)}
                    fullWidth
                    multiline
                    minRows={4}
                />
            </FormControl>
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

            <Button type="submit"  variant="contained" size="medium">
                Save
            </Button>
            </DialogActions>
            </Box>
        </Dialog>
        
    );
}

export default EditItemDialog;
