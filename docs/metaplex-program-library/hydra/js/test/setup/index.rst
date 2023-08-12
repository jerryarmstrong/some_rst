hydra/js/test/setup/index.ts
============================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    /* eslint-disable @typescript-eslint/no-explicit-any */
import test from 'tape';

export * from './log';
export * from './amman';

export function killStuckProcess() {
  test.onFinish(() => process.exit(0));
}

export function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


