packages/test-config/setup-webcrypto.ts
=======================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import crypto from 'node:crypto';

if (typeof globalThis.crypto === 'undefined') {
    Object.defineProperty(globalThis, 'crypto', {
        value: crypto.webcrypto,
        writable: true, // Allow tests to delete it.
    });
}
if (typeof globalThis.crypto.subtle === 'undefined') {
    Object.defineProperty(globalThis.crypto, 'subtle', {
        value: crypto.webcrypto.subtle,
    });
}


