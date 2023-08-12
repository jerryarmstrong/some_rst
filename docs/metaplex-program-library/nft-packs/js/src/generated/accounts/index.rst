nft-packs/js/src/generated/accounts/index.ts
============================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    export * from './PackCard';
export * from './PackConfig';
export * from './PackSet';
export * from './PackVoucher';
export * from './ProvingProcess';

import { PackCard } from './PackCard';
import { PackConfig } from './PackConfig';
import { PackSet } from './PackSet';
import { PackVoucher } from './PackVoucher';
import { ProvingProcess } from './ProvingProcess';

export const accountProviders = { PackCard, PackConfig, PackSet, PackVoucher, ProvingProcess };


