app/src/hooks/use-breakpoints.ts
================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import { useMediaQuery, useTheme } from "@mui/material";

export default () => {
  const { breakpoints } = useTheme();
  const { desktop, tablet } = breakpoints.values;

  const isMobile = useMediaQuery(breakpoints.down(tablet));
  const isDesktop = useMediaQuery(breakpoints.up(desktop + 1));

  return {
    isDesktop,
    isLaptop: !isMobile,
    isMobile,
    isTablet: !isMobile,
  };
};


