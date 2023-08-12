packages/test-config/setup-dev-mode.ts
======================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    globalThis.__DEV__ = false;
beforeEach(() => {
    globalThis.__DEV__ = false;
});


