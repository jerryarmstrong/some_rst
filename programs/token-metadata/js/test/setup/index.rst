programs/token-metadata/js/test/setup/index.ts
==============================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: ts

    import test from 'tape';

export * from './amman';
export * from './txs-init';
export * from './log';
export * from './lut';

export function killStuckProcess() {
  test.onFinish(() => process.exit(0));
}

export function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


