packages/test-config/global.d.ts
================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    declare namespace globalThis {
    // eslint-disable-next-line no-var
    var __DEV__: boolean;
    // eslint-disable-next-line no-var
    var __VERSION__: string;
}


