import AppBar from "@mui/material/AppBar";
import Avatar from "@mui/material/Avatar";
import IconButton from "@mui/material/IconButton";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import MenuIcon from "@mui/icons-material/Menu";


function Header() {
  return (
    <AppBar component="header" position="static">
        <Toolbar>
            <IconButton color="inherit" edge="start" sx={{ mr: 2 }} aria-label="Open menu">
                <MenuIcon/>
            </IconButton>
            <Typography component="h1" variant="h6" sx={{ flexGrow: 1 }}>
                SmartCart
            </Typography>
            <IconButton color="inherit" edge="end" aria-label="Open user profile">
                <Avatar sx={{ width: 32, height: 32 }}>
                    LM
                </Avatar>
            </IconButton>
        </Toolbar>
    </AppBar>    
  
  );
}

export default Header;
