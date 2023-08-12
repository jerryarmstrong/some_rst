packages/wallets/ledger/src/polyfills/Buffer.ts
===============================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: ts

    import { Buffer } from 'buffer';

if (typeof window !== 'undefined' && window.Buffer === undefined) {
    (window as any).Buffer = Buffer;
}

export {};


