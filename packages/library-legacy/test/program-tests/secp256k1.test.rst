packages/library-legacy/test/program-tests/secp256k1.test.ts
============================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import {Buffer} from 'buffer';
import {keccak_256} from '@noble/hashes/sha3';

import {
  ecdsaSign,
  isValidPrivateKey,
  publicKeyCreate,
} from '../../src/utils/secp256k1';
import {
  Connection,
  Keypair,
  sendAndConfirmTransaction,
  LAMPORTS_PER_SOL,
  Transaction,
  Secp256k1Program,
} from '../../src';
import {url} from '../url';

const randomPrivateKey = () => {
  let privateKey;
  do {
    privateKey = Keypair.generate().secretKey.slice(0, 32);
  } while (!isValidPrivateKey(privateKey));
  return privateKey;
};

if (process.env.TEST_LIVE) {
  describe('secp256k1', () => {
    const privateKey = randomPrivateKey();
    const publicKey = publicKeyCreate(
      privateKey,
      false /* isCompressed */,
    ).slice(1);
    const ethAddress = Secp256k1Program.publicKeyToEthAddress(publicKey);
    const from = Keypair.generate();
    const connection = new Connection(url, 'confirmed');

    before(async function () {
      await connection.confirmTransaction(
        await connection.requestAirdrop(from.publicKey, 10 * LAMPORTS_PER_SOL),
      );
    });

    it('create secp256k1 instruction with string address', async () => {
      const message = Buffer.from('string address');
      const messageHash = Buffer.from(keccak_256(message));
      const [signature, recoveryId] = ecdsaSign(messageHash, privateKey);
      const transaction = new Transaction().add(
        Secp256k1Program.createInstructionWithEthAddress({
          ethAddress: ethAddress.toString('hex'),
          message,
          signature,
          recoveryId,
        }),
      );

      await sendAndConfirmTransaction(connection, transaction, [from]);
    });

    it('create secp256k1 instruction with 0x prefix string address', async () => {
      const message = Buffer.from('0x string address');
      const messageHash = Buffer.from(keccak_256(message));
      const [signature, recoveryId] = ecdsaSign(messageHash, privateKey);
      const transaction = new Transaction().add(
        Secp256k1Program.createInstructionWithEthAddress({
          ethAddress: '0x' + ethAddress.toString('hex'),
          message,
          signature,
          recoveryId,
        }),
      );

      await sendAndConfirmTransaction(connection, transaction, [from]);
    });

    it('create secp256k1 instruction with buffer address', async () => {
      const message = Buffer.from('buffer address');
      const messageHash = Buffer.from(keccak_256(message));
      const [signature, recoveryId] = ecdsaSign(messageHash, privateKey);
      const transaction = new Transaction().add(
        Secp256k1Program.createInstructionWithEthAddress({
          ethAddress,
          message,
          signature,
          recoveryId,
        }),
      );

      await sendAndConfirmTransaction(connection, transaction, [from]);
    });

    it('create secp256k1 instruction with public key', async () => {
      const message = Buffer.from('public key');
      const messageHash = Buffer.from(keccak_256(message));
      const [signature, recoveryId] = ecdsaSign(messageHash, privateKey);
      const transaction = new Transaction().add(
        Secp256k1Program.createInstructionWithPublicKey({
          publicKey,
          message,
          signature,
          recoveryId,
        }),
      );

      await sendAndConfirmTransaction(connection, transaction, [from]);
    });

    it('create secp256k1 instruction with private key', async () => {
      const message = Buffer.from('private key');
      const transaction = new Transaction().add(
        Secp256k1Program.createInstructionWithPrivateKey({
          privateKey,
          message,
        }),
      );

      await sendAndConfirmTransaction(connection, transaction, [from]);
    });
  });
}


