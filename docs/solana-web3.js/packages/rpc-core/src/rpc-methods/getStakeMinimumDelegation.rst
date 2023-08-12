packages/rpc-core/src/rpc-methods/getStakeMinimumDelegation.ts
==============================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Commitment, LamportsUnsafeBeyond2Pow53Minus1, RpcResponse } from './common';

type GetStakeMinimumDelegationApiResponse = RpcResponse<LamportsUnsafeBeyond2Pow53Minus1>;

export interface GetStakeMinimumDelegationApi {
    /**
     * Returns the stake minimum delegation, in lamports.
     */
    getStakeMinimumDelegation(
        config?: Readonly<{
            commitment?: Commitment;
        }>
    ): GetStakeMinimumDelegationApiResponse;
}


