packages/sdk/core/src/utils/toBN.ts
===================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { BigNumber } from 'bignumber.js';
import BN from 'bn.js';

export function toBN(num: null): null;
export function toBN(num: undefined): undefined;
export function toBN(num: BN | BigNumber): BN;
export function toBN(num: BN | BigNumber | undefined): BN | undefined;
export function toBN(num: BN | BigNumber | null): BN | null;
export function toBN(num?: BN | BigNumber | null) {
  if (!num) {
    return num;
  }

  return new BN(num.toString());
}


