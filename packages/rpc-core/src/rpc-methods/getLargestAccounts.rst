packages/rpc-core/src/rpc-methods/getLargestAccounts.ts
=======================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { Commitment, LamportsUnsafeBeyond2Pow53Minus1, RpcResponse } from './common';

type GetLargestAccountsResponseItem = Readonly<{
    /** Base-58 encoded address of the account */
    address: Base58EncodedAddress;
    /** Number of lamports in the account */
    lamports: LamportsUnsafeBeyond2Pow53Minus1;
}>;

type GetLargestAccountsApiResponse = RpcResponse<GetLargestAccountsResponseItem[]>;

export interface GetLargestAccountsApi {
    /**
     * Returns the 20 largest accounts, by lamport balance
     * (results may be cached up to two hours)
     */
    getLargestAccounts(
        config?: Readonly<{
            commitment?: Commitment;
            /** Filter results by account type */
            filter?: 'circulating' | 'nonCirculating';
        }>
    ): GetLargestAccountsApiResponse;
}


