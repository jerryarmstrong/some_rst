packages/lending/src/utils/utils.ts
===================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { utils, KnownTokenMap } from '@oyster/common';
import { PoolInfo } from '../models';

export function getPoolName(
  map: KnownTokenMap,
  pool: PoolInfo,
  shorten = true,
) {
  const sorted = pool.pubkeys.holdingMints.map(a => a.toBase58()).sort();
  return sorted.map(item => utils.getTokenName(map, item, shorten)).join('/');
}


