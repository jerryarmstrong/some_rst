js/packages/web/src/actions/sendSignMetadata.ts
===============================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { Keypair, Connection, TransactionInstruction } from '@solana/web3.js';
import {
  sendTransactionWithRetry,
  signMetadata,
  StringPublicKey,
  WalletSigner,
} from '@oyster/common';
import { WalletNotConnectedError } from '@solana/wallet-adapter-base';

export async function sendSignMetadata(
  connection: Connection,
  wallet: WalletSigner,
  metadata: StringPublicKey,
) {
  if (!wallet.publicKey) throw new WalletNotConnectedError();

  const signers: Keypair[] = [];
  const instructions: TransactionInstruction[] = [];

  await signMetadata(metadata, wallet.publicKey.toBase58(), instructions);

  await sendTransactionWithRetry(
    connection,
    wallet,
    instructions,
    signers,
    'single',
  );
}


