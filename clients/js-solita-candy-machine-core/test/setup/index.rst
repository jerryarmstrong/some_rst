clients/js-solita-candy-machine-core/test/setup/index.ts
========================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import test from 'tape';

export * from './amman';
export * from './txs-init';
export * from './log';

export const METAPLEX_RULE_SET = new PublicKey('eBJLFYPxJmMGKuFwpDWkzxZeUrad92kZRC5BJLpzyT9');

export function killStuckProcess() {
  test.onFinish(() => process.exit(0));
}

export function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


