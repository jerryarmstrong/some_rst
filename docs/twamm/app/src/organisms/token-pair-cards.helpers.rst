app/src/organisms/token-pair-cards.helpers.ts
=============================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import type { TokenPair } from "@twamm/types";
import { populateStats } from "../domain/token-pair-details";

export const populate = (
  pair: Pick<TokenPair, "statsA" | "statsB" | "configA" | "configB">
) => {
  const { a, b, fee, orderVolume, settledVolume, routedVolume } =
    populateStats(pair);

  return {
    aMint: a,
    bMint: b,
    fee,
    id: `${a}-${b}`,
    orderVolume,
    routedVolume,
    settledVolume,
  };
};


