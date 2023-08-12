tests/create.test.ts
====================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: ts

    import test from 'tape';
import {Amman, LOCALHOST} from '@metaplex-foundation/amman';
import * as web3 from '@solana/web3.js';
import {Connection, Keypair, PublicKey, Transaction, TransactionInstruction} from '@solana/web3.js';
import debug from 'debug';
import * as beetSolana from '@metaplex-foundation/beet-solana';
import * as beet from '@metaplex-foundation/beet';
import {DigitalAssetTypes} from "../ts/generated/models";
import uuid from "uuid";
import nacl from 'tweetnacl';
import {sha3_512} from "js-sha3";

const persistLabelsPath = process.env.ADDRESS_LABEL_PATH;
const PROGRAM = new PublicKey("assetbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s");
export const logDebug = debug('dasset:test:debug');

export async function init() {
    const a = Amman.instance();
    const [payer, payerPair] = await a.addr.genLabeledKeypair('payer');
    const connection = new Connection(LOCALHOST, 'confirmed');
    const transactionHandler = a.payerTransactionHandler(connection, payerPair);
    await a.airdrop(connection, payer, 2);
    return {
        a,
        transactionHandler,
        connection,
        payer,
        payerPair
    };
}


import IAction = DigitalAssetTypes.IAction;
import Interface = DigitalAssetTypes.Interface;
import Action = DigitalAssetTypes.Action;
import ICreateAssetV1 = DigitalAssetTypes.ICreateAssetV1;

export type Creator = {
    address: web3.PublicKey;
    verified: boolean;
    share: number;
};

/**
 * @category userTypes
 * @category generated
 */
export const creatorBeet = new beet.BeetArgsStruct<Creator>(
    [
        ['address', beetSolana.publicKey],
        ['verified', beet.bool],
        ['share', beet.u8],
    ],
    'Creator',
);


test("Create An Identity", async () => {
    const {a, transactionHandler, connection, payer, payerPair} = await init();

    let [owner, ownerPair] = await a.addr.genLabeledKeypair("🔨 Owner 1");
    let idbuf = new Buffer(16);
    uuid.v4(null, idbuf)
    let [id, bump] = await PublicKey.findProgramAddress([
        Buffer.from("asset"),
        idbuf
    ], PROGRAM);
    await a.addr.addLabel("Asset", id);
    let g = new Transaction();
    let createIdentity: ICreateAssetV1 = {

    };
    let action: IAction = {
        standard: Interface.NFT,
        data: {discriminator: 1, value: createIdentity}
    };

    g.add(new TransactionInstruction({
        data: Buffer.from(Action.encode(action)),
        programId: PROGRAM,
        keys: [

        ]
    }));

    let tx = await transactionHandler.sendAndConfirmTransaction(g, [
        payerPair
    ], {skipPreflight: true}, "🤓 Testing DAS Asset Creation");


});

