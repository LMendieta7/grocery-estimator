import Paper from "@mui/material/Paper";
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
            <Box
                sx={{
                    display: "flex",
                    justifyContent: "space-between",
                }}
            >
                <Typography fontWeight={600}>
                    {shoppingListDetail.checked_count ?? 0} /{" "}
                    {shoppingListDetail.total_count ?? 0} checked
                </Typography>
                {shoppingListDetail.estimated_total != null && (
                    <Typography fontWeight={600}>
                        ${shoppingListDetail.estimated_total}
                    </Typography>
                )}
            </Box>
        </Paper>
    );

}
export default SummaryBar;
