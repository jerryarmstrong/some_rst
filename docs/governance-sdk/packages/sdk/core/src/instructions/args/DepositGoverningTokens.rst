packages/sdk/core/src/instructions/args/DepositGoverningTokens.ts
=================================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { BigNumber } from 'bignumber.js';
import type BN from 'bn.js';

import { toBigNumber } from '../../utils/toBigNumber';
import { InstructionType } from '../InstructionType';

export class DepositGoverningTokens {
  instruction = InstructionType.DepositGoverningTokens;
  amount: BigNumber;

  constructor(args: { amount: BigNumber | BN }) {
    this.amount = toBigNumber(args.amount);
  }
}


