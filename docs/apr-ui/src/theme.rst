src/theme.ts
============

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: ts

    import { createTheme } from "@mui/material/styles";

// Create a theme instance.
const theme = createTheme({
  typography: {
    fontFamily: 'Inter',
  },
  palette: {
    primary: {
      main: "#fafafa",
    },
    secondary: {
      main: "#212121",
    },
  },
});

export default theme;


