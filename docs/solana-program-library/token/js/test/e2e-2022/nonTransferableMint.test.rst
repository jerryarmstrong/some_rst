token/js/test/e2e-2022/nonTransferableMint.test.ts
==================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import chai, { expect } from 'chai';
import chaiAsPromised from 'chai-as-promised';
chai.use(chaiAsPromised);

import {
    sendAndConfirmTransaction,
    Connection,
    Keypair,
    PublicKey,
    Signer,
    SystemProgram,
    Transaction,
} from '@solana/web3.js';
import {
    createInitializeMintInstruction,
    createInitializeNonTransferableMintInstruction,
    createInitializeImmutableOwnerInstruction,
    createInitializeAccountInstruction,
    mintTo,
    getAccountLen,
    getMint,
    getMintLen,
    getNonTransferable,
    transfer,
    ExtensionType,
} from '../../src';
import { TEST_PROGRAM_ID, newAccountWithLamports, getConnection } from '../common';

const TEST_TOKEN_DECIMALS = 2;
const EXTENSIONS = [ExtensionType.NonTransferable];
describe('nonTransferable', () => {
    let connection: Connection;
    let payer: Signer;
    let mint: PublicKey;
    let mintAuthority: Keypair;
    before(async () => {
        connection = await getConnection();
        payer = await newAccountWithLamports(connection, 1000000000);
        mintAuthority = Keypair.generate();
    });
    beforeEach(async () => {
        const mintKeypair = Keypair.generate();
        mint = mintKeypair.publicKey;
        const mintLen = getMintLen(EXTENSIONS);
        const lamports = await connection.getMinimumBalanceForRentExemption(mintLen);

        const transaction = new Transaction().add(
            SystemProgram.createAccount({
                fromPubkey: payer.publicKey,
                newAccountPubkey: mint,
                space: mintLen,
                lamports,
                programId: TEST_PROGRAM_ID,
            }),
            createInitializeNonTransferableMintInstruction(mint, TEST_PROGRAM_ID),
            createInitializeMintInstruction(mint, TEST_TOKEN_DECIMALS, mintAuthority.publicKey, null, TEST_PROGRAM_ID)
        );

        await sendAndConfirmTransaction(connection, transaction, [payer, mintKeypair], undefined);
    });
    it('fails transfer', async () => {
        const mintInfo = await getMint(connection, mint, undefined, TEST_PROGRAM_ID);
        const nonTransferable = getNonTransferable(mintInfo);
        expect(nonTransferable).to.not.be.null;

        const owner = Keypair.generate();
        const accountLen = getAccountLen([ExtensionType.ImmutableOwner]);
        const lamports = await connection.getMinimumBalanceForRentExemption(accountLen);

        const sourceKeypair = Keypair.generate();
        const source = sourceKeypair.publicKey;
        let transaction = new Transaction().add(
            SystemProgram.createAccount({
                fromPubkey: payer.publicKey,
                newAccountPubkey: source,
                space: accountLen,
                lamports,
                programId: TEST_PROGRAM_ID,
            }),
            createInitializeImmutableOwnerInstruction(source, TEST_PROGRAM_ID),
            createInitializeAccountInstruction(source, mint, owner.publicKey, TEST_PROGRAM_ID)
        );
        await sendAndConfirmTransaction(connection, transaction, [payer, sourceKeypair], undefined);

        const destinationKeypair = Keypair.generate();
        const destination = destinationKeypair.publicKey;
        transaction = new Transaction().add(
            SystemProgram.createAccount({
                fromPubkey: payer.publicKey,
                newAccountPubkey: destination,
                space: accountLen,
                lamports,
                programId: TEST_PROGRAM_ID,
            }),
            createInitializeImmutableOwnerInstruction(destination, TEST_PROGRAM_ID),
            createInitializeAccountInstruction(destination, mint, owner.publicKey, TEST_PROGRAM_ID)
        );
        await sendAndConfirmTransaction(connection, transaction, [payer, destinationKeypair], undefined);

        const amount = BigInt(1000);
        await mintTo(connection, payer, mint, source, mintAuthority, amount, [], undefined, TEST_PROGRAM_ID);

        expect(transfer(connection, payer, source, destination, owner, amount, [], undefined, TEST_PROGRAM_ID)).to.be
            .rejected;
    });
});


