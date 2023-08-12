packages/rpc-core/src/rpc-methods/getSignaturesForAddress.ts
============================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { TransactionError } from '../transaction-error';
import { TransactionSignature } from '../transaction-signature';
import { UnixTimestamp } from '../unix-timestamp';
import { Commitment, RpcResponse, Slot } from './common';

type GetSignaturesForAddressTransaction = RpcResponse<{
    /** transaction signature as base-58 encoded string */
    signature: TransactionSignature;
    /** The slot that contains the block with the transaction */
    slot: Slot;
    /** Error if transaction failed, null if transaction succeeded. */
    err: TransactionError | null;
    /** Memo associated with the transaction, null if no memo is present */
    memo: string | null;
    /** estimated production time of when transaction was processed. null if not available. */
    blockTime: UnixTimestamp | null;
    /** The transaction's cluster confirmation status */
    confirmationStatus: Commitment | null;
}>;

type GetSignaturesForAddressApiResponse = readonly GetSignaturesForAddressTransaction[];

type AllowedCommitmentForGetSignaturesForAddress = Exclude<Commitment, 'processed'>;

type GetSignaturesForAddressConfig = Readonly<{
    commitment?: AllowedCommitmentForGetSignaturesForAddress;
    /** The minimum slot that the request can be evaluated at */
    minContextSlot?: Slot;
    /** maximum transaction signatures to return (between 1 and 1,000). Default: 1000 */
    limit?: number;
    /** start searching backwards from this transaction signature. If not provided the search starts from the top of the highest max confirmed block. */
    before?: TransactionSignature;
    /** search until this transaction signature, if found before limit reached */
    until?: TransactionSignature;
}>;

export interface GetSignaturesForAddressApi {
    /**
     * Returns signatures for confirmed transactions that include the given address in their accountKeys list.
     * Returns signatures backwards in time from the provided signature or most recent confirmed block
     */
    getSignaturesForAddress(
        address: Base58EncodedAddress,
        config?: GetSignaturesForAddressConfig
    ): GetSignaturesForAddressApiResponse;
}


