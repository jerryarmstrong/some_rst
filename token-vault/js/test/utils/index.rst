token-vault/js/test/utils/index.ts
==================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import test from 'tape';

export * from './accounts';
export * from './address-labels';
export * from './asserts';
export * from './log';
export * from './token';
export * from './transactions';
export * from './vault-asserts';

export function killStuckProcess() {
  test.onFinish(() => process.exit(0));
}


