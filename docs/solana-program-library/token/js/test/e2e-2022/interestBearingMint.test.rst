token/js/test/e2e-2022/interestBearingMint.test.ts
==================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import chai, { expect } from 'chai';
import chaiAsPromised from 'chai-as-promised';
chai.use(chaiAsPromised);

import { Connection, Keypair, PublicKey, Signer } from '@solana/web3.js';
import {
    createInterestBearingMint,
    getInterestBearingMintConfigState,
    getMint,
    updateRateInterestBearingMint,
} from '../../src';
import { getConnection, newAccountWithLamports, TEST_PROGRAM_ID } from '../common';

const TEST_TOKEN_DECIMALS = 2;
const TEST_RATE = 10;
const TEST_UPDATE_RATE = 50;

describe('interestBearingMint', () => {
    let connection: Connection;
    let payer: Signer;
    let mint: PublicKey;
    let rateAuthority: Keypair;
    let mintAuthority: Keypair;
    let freezeAuthority: Keypair;
    let mintKeypair: Keypair;

    before(async () => {
        connection = await getConnection();
        payer = await newAccountWithLamports(connection, 1000000000);
        rateAuthority = Keypair.generate();
        mintAuthority = Keypair.generate();
        freezeAuthority = Keypair.generate();
    });

    it('initialize and update rate', async () => {
        mintKeypair = Keypair.generate();
        mint = mintKeypair.publicKey;
        await createInterestBearingMint(
            connection,
            payer,
            mintAuthority.publicKey,
            freezeAuthority.publicKey,
            rateAuthority.publicKey,
            TEST_RATE,
            TEST_TOKEN_DECIMALS,
            mintKeypair,
            undefined,
            TEST_PROGRAM_ID
        );
        const mintInfo = await getMint(connection, mint, undefined, TEST_PROGRAM_ID);
        const interestBearingMintConfigState = getInterestBearingMintConfigState(mintInfo);
        expect(interestBearingMintConfigState).to.not.be.null;
        if (interestBearingMintConfigState !== null) {
            expect(interestBearingMintConfigState.rateAuthority).to.eql(rateAuthority.publicKey);
            expect(interestBearingMintConfigState.preUpdateAverageRate).to.eql(TEST_RATE);
            expect(interestBearingMintConfigState.currentRate).to.eql(TEST_RATE);
            expect(interestBearingMintConfigState.lastUpdateTimestamp).to.be.greaterThan(0);
            expect(interestBearingMintConfigState.initializationTimestamp).to.be.greaterThan(0);
        }

        await updateRateInterestBearingMint(
            connection,
            payer,
            mint,
            rateAuthority,
            TEST_UPDATE_RATE,
            [],
            undefined,
            TEST_PROGRAM_ID
        );
        const mintInfoUpdatedRate = await getMint(connection, mint, undefined, TEST_PROGRAM_ID);
        const updatedRateConfigState = getInterestBearingMintConfigState(mintInfoUpdatedRate);

        expect(updatedRateConfigState).to.not.be.null;
        if (updatedRateConfigState !== null) {
            expect(updatedRateConfigState.rateAuthority).to.eql(rateAuthority.publicKey);
            expect(updatedRateConfigState.currentRate).to.eql(TEST_UPDATE_RATE);
            expect(updatedRateConfigState.preUpdateAverageRate).to.eql(TEST_RATE);
            expect(updatedRateConfigState.lastUpdateTimestamp).to.be.greaterThan(0);
            expect(updatedRateConfigState.initializationTimestamp).to.be.greaterThan(0);
        }
    });
});


