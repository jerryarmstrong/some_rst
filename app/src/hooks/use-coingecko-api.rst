app/src/hooks/use-coingecko-api.ts
==================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import { useContext } from "react";

import { ApiContext } from "../contexts/coingecko-api-context";

// FEAT: replace coingecko with jupiter
export default () => {
  const context = useContext(ApiContext);
  if (context === undefined) {
    throw new Error("Coingecko context is required");
  }
  return context.contractApi;
};


