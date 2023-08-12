packages/rpc-core/src/rpc-methods/getMinimumBalanceForRentExemption.ts
======================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Commitment, LamportsUnsafeBeyond2Pow53Minus1, RpcResponse, U64UnsafeBeyond2Pow53Minus1 } from './common';

type GetMinimumBalanceForRentExemptionApiResponse = RpcResponse<LamportsUnsafeBeyond2Pow53Minus1>;

export interface GetMinimumBalanceForRentExemptionApi {
    /**
     * Returns the minimum balance to exempt an account of a certain size from rent
     */
    getMinimumBalanceForRentExemption(
        size: U64UnsafeBeyond2Pow53Minus1,
        config?: Readonly<{
            commitment?: Commitment;
        }>
    ): GetMinimumBalanceForRentExemptionApiResponse;
}


