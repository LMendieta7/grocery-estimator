import { useState } from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import TextField from "@mui/material/TextField";

function ListDialog({ list = null, onClose, onSave }) {
    const [name, setName] = useState(list?.name ?? "");

    async function handleSubmit(event) {
        event.preventDefault();

        await onSave({
            name: name.trim(),
        });

        onClose();
    }

    return (
        <Dialog open onClose={onClose} fullWidth maxWidth="xs">
            <DialogTitle>
                {list ? "Edit Shopping List" : "Add Shopping List"}
            </DialogTitle>

            <form onSubmit={handleSubmit}>
                <DialogContent>
                    <FormControl fullWidth>
                        <FormLabel htmlFor="list-name" sx={{ mb: 0.75 }}>
                            List Name
                        </FormLabel>
                        <TextField
                            id="list-name"
                            value={name}
                            onChange={(event) => setName(event.target.value)}
                            autoFocus
                            required
                            fullWidth
                        />
                    </FormControl>
                </DialogContent>

                <DialogActions>
                    <Button onClick={onClose}>
                        Cancel
                    </Button>
                    <Button
                        type="submit"
                        variant="contained"
                        disabled={!name.trim()}
                    >
                        {list ? "Save" : "Add"}
                    </Button>
                </DialogActions>
            </form>
        </Dialog>
    );
}

export default ListDialog;
