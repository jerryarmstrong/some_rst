js/packages/web/src/views/packCreate/components/ReviewAndMintStep/utils.ts
==========================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    export const getTotalNFTsCount = (
  distributions: Record<string, number>,
): number =>
  Object.values(distributions).reduce((itemSupply, sum) => sum + itemSupply, 0);


