token/js/src/actions/internal.ts
================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import { PublicKey, Signer } from '@solana/web3.js';

/** @internal */
export function getSigners(signerOrMultisig: Signer | PublicKey, multiSigners: Signer[]): [PublicKey, Signer[]] {
    return signerOrMultisig instanceof PublicKey
        ? [signerOrMultisig, multiSigners]
        : [signerOrMultisig.publicKey, [signerOrMultisig]];
}


