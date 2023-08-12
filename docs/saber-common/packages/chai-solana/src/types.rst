packages/chai-solana/src/types.ts
=================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    /// <reference types="chai" />

import "chai-bn";
import "chai-as-promised";

import type { BigintIsh, TokenAmount } from "@coral-xyz/token-utils";
import type { Address } from "@project-serum/anchor";

declare global {
  // eslint-disable-next-line @typescript-eslint/no-namespace
  namespace Chai {
    export interface TokenAmountComparer {
      (value: TokenAmount | BigintIsh, message?: string): void;
    }

    export interface TokenAmountAssertion {
      equal: TokenAmountComparer;
      equals: TokenAmountComparer;
      eq: TokenAmountComparer;
      // above: TokenAmountComparer;
      // greaterThan: TokenAmountComparer;
      // gt: TokenAmountComparer;
      // gte: TokenAmountComparer;
      // below: TokenAmountComparer;
      // lessThan: TokenAmountComparer;
      // lt: TokenAmountComparer;
      // lte: TokenAmountComparer;
      // least: TokenAmountComparer;
      // most: TokenAmountComparer;
      // closeTo: BNCloseTo;
      // negative: BNBoolean;
      zero: () => void;
    }

    interface Assertion {
      eqAddress: (otherKey: Address, message?: string) => Assertion;
      eqAmount: (otherAmount: TokenAmount, message?: string) => Assertion;
      tokenAmount: TokenAmountAssertion;
    }
  }
}


