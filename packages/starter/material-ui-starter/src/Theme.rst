packages/starter/material-ui-starter/src/Theme.tsx
==================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import { createTheme, StyledEngineProvider, ThemeProvider } from '@mui/material';
import { deepPurple } from '@mui/material/colors';
import { SnackbarProvider } from 'notistack';
import type { FC, ReactNode } from 'react';
import React from 'react';

const theme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
            main: deepPurple[700],
        },
    },
    components: {
        MuiButtonBase: {
            styleOverrides: {
                root: {
                    justifyContent: 'flex-start',
                },
            },
        },
        MuiButton: {
            styleOverrides: {
                root: {
                    textTransform: 'none',
                    padding: '12px 16px',
                },
                startIcon: {
                    marginRight: 8,
                },
                endIcon: {
                    marginLeft: 8,
                },
            },
        },
    },
});

export const Theme: FC<{ children: ReactNode }> = ({ children }) => {
    return (
        <StyledEngineProvider injectFirst>
            <ThemeProvider theme={theme}>
                <SnackbarProvider>{children}</SnackbarProvider>
            </ThemeProvider>
        </StyledEngineProvider>
    );
};


