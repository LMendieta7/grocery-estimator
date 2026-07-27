import Paper from "@mui/material/Paper";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";

function SummaryBar({ shoppingListDetail }){
    return (
        <Paper
            variant="outlined"
            sx={{
                px: 2,
                py: 1.4,
                borderRadius: 1,
                bgcolor: "lightblue",
            }}
        >
            <Stack>
                <Box sx={{display:"flex",
                        justifyContent: "space-between",
        
                    }}>
                    <Typography>
                    {shoppingListDetail.checked_count ?? 0} /{" "}
                    {shoppingListDetail.total_count ?? 0} checked
                    </Typography>

                    <Typography fontWeight={600}>
                        $
                        {shoppingListDetail.estimated_total ?? "0.00"}
                    </Typography>
                </Box>
                
            </Stack>
        </Paper>
    );

}
export default SummaryBar;