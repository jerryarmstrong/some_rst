ui/src/lib/classGetters.ts
==========================

Last edited: 2023-08-09 02:22:59

Contents:

.. code-block:: ts

    import { CustodyAccount } from "@/lib/CustodyAccount";
import { PoolAccount } from "@/lib/PoolAccount";
import { PriceStats } from "@/lib/types";

export function getCurrentWeight(
  pool: PoolAccount,
  custody: CustodyAccount,
  stats: PriceStats
): number {
  let token = custody.getTokenE();
  const custodyAmount = Number(custody.assets.owned) / 10 ** custody.decimals;

  const custodyPrice = stats[token].currentPrice;

  return pool.getLiquidities(stats)
    ? (100 * custodyAmount * custodyPrice) / pool.getLiquidities(stats)
    : 0;
}


