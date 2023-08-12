packages/sdk/core/src/vote/VoteWeight.ts
========================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { BigNumber } from 'bignumber.js';
import type BN from 'bn.js';

import { toBigNumber } from '../utils/toBigNumber';

export class VoteWeight {
  yes: BigNumber;
  no: BigNumber;

  constructor(args: { yes: BigNumber | BN; no: BigNumber | BN }) {
    this.yes = toBigNumber(args.yes);
    this.no = toBigNumber(args.no);
  }
}


