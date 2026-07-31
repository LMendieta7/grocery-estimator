import { useState, useEffect } from "react";
import { searchProducts } from "../services/productApi";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";

function ProductSearch({ onAddProductToList }) {
    const [search, setSearch] = useState("");
    const [suggestions, setSuggestions] = useState([]);
    const [error, setError] = useState("");
    
    useEffect(() => {
        const searchText = search.trim();

        if (searchText.length === 0) {
            return;
        }

        const controller = new AbortController();
        const timer = setTimeout(async () => {
            try {
                const products = await searchProducts(searchText, controller.signal);
                setSuggestions(products);
                setError("");
            } catch (requestError) {
                if (requestError.name === "AbortError") {
                    return;
                }

                setSuggestions([]);
                setError("Could not search products.");
            }
        }, 300);

        return () => {
            clearTimeout(timer);
            controller.abort();
        };

    }, [search]);

    function handleSearchChange(_event, value, reason) {
        if (reason === "reset") {
            return;
        }

        setSearch(value);

        if (value.trim().length === 0) {
            setSuggestions([]);
            setError("");
        }
    }

    async function handleProductSelect(_event, product) {
        if (!product) {
            return;
        }

        try {
            await onAddProductToList(product);
            setSearch("");
            setSuggestions([]);
            setError("");
        } catch {
            setError("Could not add product to the shopping list.");
        }
    }
    
    return (
        <FormControl fullWidth>
            <FormLabel htmlFor="product-search" sx={{ mb: 0.75 }}>
                Search Products
            </FormLabel>
            <Autocomplete
                id="product-search"
                size="small"
                value={null}
                inputValue={search}
                options={suggestions}
                forcePopupIcon={false}
                getOptionLabel={(product) => product.name}
                isOptionEqualToValue={(option, value) => option.id === value.id}
                onInputChange={handleSearchChange}
                onChange={handleProductSelect}
                renderInput={(params) => (
                    <TextField
                        {...params}
                        placeholder="Start typing a product"
                        error={Boolean(error)}
                        helperText={error}
                    />
                )}
            />
        </FormControl>
    );
}

export default ProductSearch;
