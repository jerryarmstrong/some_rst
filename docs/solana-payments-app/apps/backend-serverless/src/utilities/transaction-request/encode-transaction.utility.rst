apps/backend-serverless/src/utilities/transaction-request/encode-transaction.utility.ts
=======================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import * as web3 from '@solana/web3.js';
import pkg from 'bs58';
const { encode } = pkg;

export const encodeTransaction = (transactionBytes: string): web3.Transaction => {
    const transactionBytesBuffer = Buffer.from(transactionBytes, 'base64');
    const transaction = web3.Transaction.from(transactionBytesBuffer);
    return transaction;
};

export const encodeBufferToBase58 = (buffer: Buffer): string => {
    const uint8ArrayBuffer: Uint8Array = Uint8Array.from(buffer);
    const encoded = encode(uint8ArrayBuffer);
    return encoded;
};


