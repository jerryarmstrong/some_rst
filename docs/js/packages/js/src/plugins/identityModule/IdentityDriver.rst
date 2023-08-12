packages/js/src/plugins/identityModule/IdentityDriver.ts
========================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { IdentitySigner } from '@/types';

export type IdentityDriver = IdentitySigner & {
  secretKey?: Uint8Array;
};


