packages/test-config/setup-secure-context.ts
============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    globalThis.isSecureContext = true;
beforeEach(() => {
    globalThis.isSecureContext = true;
});


