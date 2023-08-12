app/validators/accounts/nonce.ts
================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    /* eslint-disable @typescript-eslint/no-redeclare */

import { PublicKeyFromString } from '@validators/pubkey';
import { enums, Infer, string, type } from 'superstruct';

export type NonceAccountType = Infer<typeof NonceAccountType>;
export const NonceAccountType = enums(['uninitialized', 'initialized']);

export type NonceAccountInfo = Infer<typeof NonceAccountInfo>;
export const NonceAccountInfo = type({
    authority: PublicKeyFromString,
    blockhash: string(),
    feeCalculator: type({
        lamportsPerSignature: string(),
    }),
});

export type NonceAccount = Infer<typeof NonceAccount>;
export const NonceAccount = type({
    info: NonceAccountInfo,
    type: NonceAccountType,
});


