examples/js/ui-create-nft/pages/useUmi.ts
=========================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: ts

    import type { Umi } from "@metaplex-foundation/umi";
import { createContext, useContext } from "react";

type UmiContext = {
  umi: Umi | null;
};

const DEFAULT_CONTEXT: UmiContext = {
  umi: null,
};

export const UmiContext = createContext<UmiContext>(DEFAULT_CONTEXT);

export function useUmi(): Umi {
  const umi = useContext(UmiContext).umi;
  if (!umi) {
    throw new Error(
      "Umi context was not initialized. " +
        "Did you forget to wrap your app with <UmiProvider />?"
    );
  }
  return umi;
}


