src/views/margin/newPosition/interfaces.tsx
===========================================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: tsx

    import { ParsedAccount } from "../../../contexts/accounts";
import { LendingReserve } from "../../../models/lending/reserve";

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


