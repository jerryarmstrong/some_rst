packages/rpc-core/src/rpc-methods/requestAirdrop.ts
===================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { Base58EncodedTransactionSignature, Commitment, LamportsUnsafeBeyond2Pow53Minus1 } from './common';

type RequestAirdropConfig = Readonly<{
    commitment?: Commitment;
}>;

type RequestAirdropResponse = Base58EncodedTransactionSignature;

export interface RequestAirdropApi {
    /**
     * Requests an airdrop of lamports to a Pubkey
     */
    requestAirdrop(
        recipientAccount: Base58EncodedAddress,
        lamports: LamportsUnsafeBeyond2Pow53Minus1,
        config?: RequestAirdropConfig
    ): RequestAirdropResponse;
}


