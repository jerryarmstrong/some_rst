packages/sdk/core/src/utils/toBigNumber.ts
==========================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { BigNumber } from 'bignumber.js';
import type BN from 'bn.js';

export function toBigNumber(num: null): null;
export function toBigNumber(num: undefined): undefined;
export function toBigNumber(num: BN | BigNumber): BigNumber;
export function toBigNumber(num: BN | BigNumber | undefined): BigNumber | undefined;
export function toBigNumber(num: BN | BigNumber | null): BigNumber | null;
export function toBigNumber(num?: BN | BigNumber | null) {
  if (!num) {
    return num;
  }

  return new BigNumber(num.toString());
}


