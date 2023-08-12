packages/library-legacy/test/message-tests/legacy.test.ts
=========================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import bs58 from 'bs58';
import {expect} from 'chai';
import {sha256} from '@noble/hashes/sha256';

import {Message} from '../../src/message';
import {TransactionInstruction} from '../../src/transaction';
import {PublicKey} from '../../src/publickey';

function createTestKeys(count: number): Array<PublicKey> {
  return new Array(count).fill(0).map(() => PublicKey.unique());
}

describe('Message', () => {
  it('compile', () => {
    const keys = createTestKeys(5);
    const recentBlockhash = bs58.encode(sha256('test'));
    const payerKey = keys[0];
    const instructions = [
      new TransactionInstruction({
        programId: keys[4],
        keys: [
          {pubkey: keys[1], isSigner: true, isWritable: true},
          {pubkey: keys[2], isSigner: false, isWritable: false},
          {pubkey: keys[3], isSigner: false, isWritable: false},
        ],
        data: Buffer.alloc(1),
      }),
      new TransactionInstruction({
        programId: keys[1],
        keys: [
          {pubkey: keys[2], isSigner: true, isWritable: false},
          {pubkey: keys[3], isSigner: false, isWritable: true},
        ],
        data: Buffer.alloc(2),
      }),
    ];

    const message = Message.compile({
      payerKey,
      recentBlockhash,
      instructions,
    });

    expect(message.accountKeys).to.eql([
      payerKey, // payer is first
      keys[1], // other writable signer
      keys[2], // sole readonly signer
      keys[3], // sole writable non-signer
      keys[4], // sole readonly non-signer
    ]);
    expect(message.header).to.eql({
      numRequiredSignatures: 3,
      numReadonlySignedAccounts: 1,
      numReadonlyUnsignedAccounts: 1,
    });
    expect(message.addressTableLookups.length).to.eq(0);
    expect(message.instructions).to.eql([
      {
        programIdIndex: 4,
        accounts: [1, 2, 3],
        data: bs58.encode(Buffer.alloc(1)),
      },
      {
        programIdIndex: 1,
        accounts: [2, 3],
        data: bs58.encode(Buffer.alloc(2)),
      },
    ]);
    expect(message.recentBlockhash).to.eq(recentBlockhash);
  });

  it('compile without instructions', () => {
    const payerKey = PublicKey.unique();
    const recentBlockhash = bs58.encode(sha256('test'));
    const message = Message.compile({
      payerKey,
      instructions: [],
      recentBlockhash,
    });

    expect(message.accountKeys).to.eql([payerKey]);
    expect(message.header).to.eql({
      numRequiredSignatures: 1,
      numReadonlySignedAccounts: 0,
      numReadonlyUnsignedAccounts: 0,
    });
    expect(message.addressTableLookups.length).to.eq(0);
    expect(message.instructions.length).to.eq(0);
    expect(message.recentBlockhash).to.eq(recentBlockhash);
  });

  it('isAccountWritable', () => {
    const accountKeys = [
      PublicKey.unique(),
      PublicKey.unique(),
      PublicKey.unique(),
      PublicKey.unique(),
    ];

    const recentBlockhash = bs58.encode(sha256('test'));
    const message = new Message({
      header: {
        numRequiredSignatures: 2,
        numReadonlySignedAccounts: 1,
        numReadonlyUnsignedAccounts: 1,
      },
      recentBlockhash,
      accountKeys,
      instructions: [],
    });

    expect(message.isAccountWritable(0)).to.be.true;
    expect(message.isAccountWritable(1)).to.be.false;
    expect(message.isAccountWritable(2)).to.be.true;
    expect(message.isAccountWritable(3)).to.be.false;
  });

  it('isAccountSigner', () => {
    const accountKeys = [
      PublicKey.unique(),
      PublicKey.unique(),
      PublicKey.unique(),
      PublicKey.unique(),
    ];

    const recentBlockhash = bs58.encode(sha256('test'));
    const message = new Message({
      header: {
        numRequiredSignatures: 2,
        numReadonlySignedAccounts: 1,
        numReadonlyUnsignedAccounts: 1,
      },
      recentBlockhash,
      accountKeys,
      instructions: [],
    });

    expect(message.isAccountSigner(0)).to.be.true;
    expect(message.isAccountSigner(1)).to.be.true;
    expect(message.isAccountSigner(2)).to.be.false;
    expect(message.isAccountSigner(3)).to.be.false;
  });
});


