examples/point-of-sale/src/client/hooks/useTheme.ts
===================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { createContext, useContext } from 'react';

export type Theme = 'light' | 'dark';

export interface ThemeContextState {
    theme: Theme;
    setTheme(theme: Theme): void;
}

export const ThemeContext = createContext<ThemeContextState>({} as ThemeContextState);

export function useTheme(): ThemeContextState {
    return useContext(ThemeContext);
}


