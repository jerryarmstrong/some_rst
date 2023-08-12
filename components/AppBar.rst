components/AppBar.tsx
=====================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import Link from "next/link";

export default function WalletButtonAppBar() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static" sx={{ backgroundColor: "#2a2a2a" }}>
                <Toolbar>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                        <Link href={"/"}>
                            🍰 Trifle UI
                        </Link>
                    </Typography>
                    <WalletMultiButton />
                </Toolbar>
            </AppBar>
        </Box>
    );
}

