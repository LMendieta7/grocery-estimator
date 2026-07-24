import Paper from "@mui/material/Paper";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
// checked_count: int
//     total_count: int
//     estimated_total: Decimal

function SummaryBar({ shoppingListDetail }){
    return (
        <Paper
            variant="outlined"
            sx={{
                px: 2,
                py: 1.5,
                borderRadius: 2,
                bgcolor: "inherit",
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