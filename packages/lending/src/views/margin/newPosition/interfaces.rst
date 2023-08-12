packages/lending/src/views/margin/newPosition/interfaces.tsx
============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { ParsedAccount } from '@oyster/common';
import { LendingReserve } from '../../../models/lending/reserve';

export interface Token {
  mintAddress: string;
  tokenName: string;
  tokenSymbol: string;
}

export interface Position {
  id?: number | null;
  leverage: number;
  collateral: {
    type?: ParsedAccount<LendingReserve>;
    value?: number | null;
  };
  asset: {
    type?: ParsedAccount<LendingReserve>;
    value?: number | null;
  };
  error?: string;
}


