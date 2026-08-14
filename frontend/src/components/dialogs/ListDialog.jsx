import { useState } from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import Box from "@mui/material/Box";



function ListDialog({list = null, onClose, onSave}){
    const [listName, setListName] = useState(list?.name ?? "");
    const isEditing = Boolean(list);

    async function handleSubmit(event) {
        event.preventDefault();
        const list = {
            name: listName.trim()
        };

        await onSave(list);
        onClose();
    }


    return (

        <Dialog
            open
            onClose={onClose}
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
            <DialogTitle sx={{mb:0, pb:0}} align="center"> {isEditing ? "Edit List" : "Create List"}</DialogTitle>
            <Box
                component="form"
                onSubmit={handleSubmit}
                sx={{
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
            <DialogContent>
            
            <FormControl fullWidth size="small" margin="dense">
                <FormLabel htmlFor="list-name" sx={{ mb: 0.75 }}>
                    List Name
                </FormLabel>
                <TextField
                    id="list-name"
                    value={listName}
                    onChange={(event) => setListName(event.target.value)}
                    size="small"
                    required
                    fullWidth
                />
            </FormControl>
            
            </DialogContent>

            <DialogActions sx={{ px: 3, pb: 2, bgcolor: "inherit" }}>

                <Button type="button" size="medium" onClick={onClose}>
                    Cancel
                </Button>

                <Button type="submit"  variant="contained" size="medium">
                    {isEditing ? "Save" : "Create"}
                </Button>
            </DialogActions>
            </Box>
        </Dialog>
        
    );
}

export default ListDialog;
