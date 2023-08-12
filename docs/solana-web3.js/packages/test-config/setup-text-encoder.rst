packages/test-config/setup-text-encoder.ts
==========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { TextEncoder } from 'util';

if (typeof globalThis.TextEncoder === 'undefined') {
    globalThis.TextEncoder = TextEncoder;
}


