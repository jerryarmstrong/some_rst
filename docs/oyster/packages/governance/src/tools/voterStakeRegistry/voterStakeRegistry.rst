packages/governance/src/tools/voterStakeRegistry/voterStakeRegistry.ts
======================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import BN from 'bn.js';
import { BigNumber } from 'bignumber.js';

export const SCALED_FACTOR_SHIFT = 9;

export function getScaledFactor(amount: number) {
  return new BN(
    new BigNumber(amount.toString()).shiftedBy(SCALED_FACTOR_SHIFT).toString(),
  );
}


