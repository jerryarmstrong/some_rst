packages/sdk/test/setup/index.ts
================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import test from 'tape';

export * from './amman';
export * from './txs-init';
export * from './log';

export function killStuckProcess() {
  test.onFinish(() => process.exit(0));
}

export function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


