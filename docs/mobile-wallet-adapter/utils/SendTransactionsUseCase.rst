utils/SendTransactionsUseCase.tsx
=================================

Last edited: 2023-04-24 04:07:06

Contents:

.. code-block:: tsx

    import {
  Connection,
  VersionedTransaction,
  TransactionSignature,
  SendOptions,
  clusterApiUrl,
} from '@solana/web3.js';
import {decode} from 'bs58';

export class SendTransactionsError extends Error {
  valid: boolean[];
  constructor(message: string, valid: boolean[]) {
    super(message);
    this.name = 'SendTransactionErrors';
    this.valid = valid;
  }
}

export class SendTransactionsUseCase {
  static readonly SIGNATURE_LEN = 64;
  static readonly PUBLIC_KEY_LEN = 32;

  static async sendSignedTransactions(
    signedTransactions: Array<Uint8Array>,
    minContextSlot: number | undefined,
  ): Promise<number[][]> {
    const connection = new Connection(clusterApiUrl('testnet'), 'finalized');
    const signatures: (number[] | null)[] = await Promise.all(
      signedTransactions.map(async byteArray => {
        // Try sending a transaction.
        try {
          const transaction: VersionedTransaction =
            VersionedTransaction.deserialize(byteArray);

          const sendOptions: SendOptions = {
            minContextSlot: minContextSlot,
            preflightCommitment: 'processed',
          };
          const signature: TransactionSignature =
            await connection.sendTransaction(transaction, sendOptions); // here
          const decoded = decode(signature);
          return Array.from(decoded);
        } catch (error) {
          console.log('Failed sending transaction ' + error);
          return null;
        }
      }),
    );

    if (signatures.includes(null)) {
      const valid = signatures.map(signature => {
        return signature !== null;
      });
      throw new SendTransactionsError('Failed sending transactions', valid);
    }

    return signatures as number[][];
  }
}


