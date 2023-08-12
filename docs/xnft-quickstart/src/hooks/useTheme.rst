src/hooks/useTheme.tsx
======================

Last edited: 2023-07-18 02:03:22

Contents:

.. code-block:: tsx

    import { useColorScheme } from "./xnft-hooks";

export function useTheme() {
  const colorScheme = useColorScheme();
  const theme = colorScheme === "dark" ? darkTheme : lightTheme;

  return {
    custom: theme,
    colorScheme,
  };
}

const darkTheme = {
  backgroundColor: "black",
  fontColor: "white",
};

const lightTheme = {
  backgroundColor: "white",
  fontColor: "black",
};


