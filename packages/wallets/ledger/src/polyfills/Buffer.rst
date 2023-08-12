packages/wallets/ledger/src/polyfills/Buffer.ts
===============================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: ts

    import { Buffer } from 'buffer';

if (typeof window !== 'undefined' && window.Buffer === undefined) {
    (window as any).Buffer = Buffer;
}

export {};


