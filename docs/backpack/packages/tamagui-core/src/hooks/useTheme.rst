packages/tamagui-core/src/hooks/useTheme.tsx
============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    // recoil is only here because of useDarkMode. there's a better way to do this but still TBD
import { useDarkMode } from "@coral-xyz/recoil"; // eslint-disable-line
import { MOBILE_DARK_THEME, MOBILE_LIGHT_THEME } from "@coral-xyz/themes";

export function useCustomTheme() {
  const isDarkMode = useDarkMode();
  const theme = isDarkMode ? MOBILE_DARK_THEME : MOBILE_LIGHT_THEME;

  return {
    custom: theme.custom,
    colorScheme: isDarkMode ? "dark" : "light",
  };
}


