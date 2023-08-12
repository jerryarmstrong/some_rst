src/providers/mints/index.tsx
=============================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { LargestAccountsProvider } from "./largest";
import { TokenRegistryProvider } from "./token-registry";

type ProviderProps = { children: React.ReactNode };
export function MintsProvider({ children }: ProviderProps) {
  return (
    <TokenRegistryProvider>
      <LargestAccountsProvider>{children}</LargestAccountsProvider>
    </TokenRegistryProvider>
  );
}


