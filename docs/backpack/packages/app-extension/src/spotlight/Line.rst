packages/app-extension/src/spotlight/Line.tsx
=============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useCustomTheme } from "@coral-xyz/themes";

export const Line = () => {
  const theme = useCustomTheme();

  return (
    <div style={{ height: 1, background: theme.custom.colors.icon }} />
  );
};


