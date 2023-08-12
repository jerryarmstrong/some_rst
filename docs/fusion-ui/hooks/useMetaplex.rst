hooks/useMetaplex.ts
====================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: ts

    import { Metaplex } from "@metaplex-foundation/js";
import { createContext, useContext } from "react";
import { PROGRAM_ID } from "@metaplex-foundation/mpl-token-metadata";


interface MetaplexContextInterface {
  metaplex: Metaplex | null;
}

const defaultContext = {
  metaplex: null,
};

export const MetaplexContext = createContext<MetaplexContextInterface>(
  defaultContext,
);

export function useMetaplex() {
  let ctx = useContext(MetaplexContext);
  return ctx;
}


