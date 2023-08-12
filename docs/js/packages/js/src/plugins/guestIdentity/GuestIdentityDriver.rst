packages/js/src/plugins/guestIdentity/GuestIdentityDriver.ts
============================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { PublicKey, Transaction } from '@solana/web3.js';
import { IdentityDriver } from '../identityModule';
import { OperationUnauthorizedForGuestsError } from '@/errors';

export class GuestIdentityDriver implements IdentityDriver {
  public readonly publicKey: PublicKey;

  constructor(publicKey?: PublicKey) {
    this.publicKey = publicKey ?? PublicKey.default;
  }

  public async signMessage(): Promise<Uint8Array> {
    throw new OperationUnauthorizedForGuestsError('signMessage');
  }

  public async signTransaction(): Promise<Transaction> {
    throw new OperationUnauthorizedForGuestsError('signTransaction');
  }

  public async signAllTransactions(): Promise<Transaction[]> {
    throw new OperationUnauthorizedForGuestsError('signAllTransactions');
  }
}


