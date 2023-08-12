utils/deploy-serum-market.ts
============================

Last edited: 2023-03-27 09:30:13

Contents:

.. code-block:: ts

    import { MangoUtils } from "./mango_utils";
import { Connection, Keypair, LAMPORTS_PER_SOL, PublicKey } from '@solana/web3.js';
import { sleep } from "@blockworks-foundation/mango-client";
import * as fs from 'fs';
import { web3, BN } from "@project-serum/anchor";
import * as splToken from "@solana/spl-token";
import { Market, DexInstructions, OpenOrders, } from "@project-serum/serum";
import {
    SystemProgram,
    TransactionInstruction,
    Transaction,
    sendAndConfirmTransaction,
    Signer,
} from "@solana/web3.js";

interface CreateMarketInfo {
    baseToken: PublicKey;
    quoteToken: PublicKey;
    baseLotSize: number;
    quoteLotSize: number;
    feeRateBps: number;
}

async function createAccount(conn: Connection, owner: Keypair, pid: PublicKey, space: number): Promise<Keypair> {
    const newAccount = new Keypair();
    const createTx = new Transaction().add(
        SystemProgram.createAccount({
            fromPubkey: owner.publicKey,
            newAccountPubkey: newAccount.publicKey,
            programId: pid,
            lamports: await conn.getMinimumBalanceForRentExemption(
                space
            ),
            space,
        })
    );

    await sendAndConfirmTransaction(conn, createTx, [
        owner,
        newAccount,
    ]);
    return newAccount;
}


async function createMarket(conn: Connection, authority: Keypair, dexProgramId: PublicKey, info: CreateMarketInfo, eventQSize : number ): Promise<Market> {
    const owner = authority;
    const market = await createAccount(conn, owner, dexProgramId, Market.getLayout(dexProgramId).span,);
    console.log('market : ' + market.publicKey.toString());
    const requestQueue = await createAccount(conn, owner, dexProgramId, 5132);
    console.log('requestQueue : ' + requestQueue.publicKey.toString());
    const eventQueue = await createAccount(conn, owner, dexProgramId, eventQSize);
    console.log('eventQueue : ' + eventQueue.publicKey.toString());
    const bids = await createAccount(conn, owner, dexProgramId, 65548);
    console.log('bids : ' + bids.publicKey.toString());
    const asks = await createAccount(conn, owner, dexProgramId, 65548);
    console.log('asks : ' + asks.publicKey.toString());
    const quoteDustThreshold = new BN(100);

    const [vaultOwner, vaultOwnerBump] = await findVaultOwner(market.publicKey, dexProgramId,);

    const [baseVault, quoteVault] = await Promise.all([
        splToken.createAccount(conn, authority, info.baseToken, vaultOwner, Keypair.generate()),
        splToken.createAccount(conn, authority, info.quoteToken, vaultOwner, Keypair.generate()),
    ]);

    console.log('vaultOwner : ' + vaultOwner.toString());
    console.log('baseVault : ' + baseVault.toString());
    console.log('quoteVault : ' + quoteVault.toString());

    const initMarketTx = new Transaction( {
        feePayer: authority.publicKey,
        recentBlockhash: (await conn.getRecentBlockhash()).blockhash,
    }
    ).add(
        DexInstructions.initializeMarket(
            toPublicKeys({
                market,
                requestQueue,
                eventQueue,
                bids,
                asks,
                baseVault,
                quoteVault,
                baseMint: info.baseToken,
                quoteMint: info.quoteToken,
                baseLotSize: new BN(info.baseLotSize),
                quoteLotSize: new BN(info.quoteLotSize),
                feeRateBps: info.feeRateBps,
                vaultSignerNonce: vaultOwnerBump,
                quoteDustThreshold,
                programId: dexProgramId,
            })
        )
    );

    await web3.sendAndConfirmTransaction(conn, initMarketTx, [authority]);

    let mkt = await Market.load(
        conn,
        market.publicKey,
        { commitment: "recent" },
        dexProgramId
    );
    console.log('Market created');
    return mkt;
}

async function findVaultOwner(market: PublicKey, dexProgramId: PublicKey): Promise<[PublicKey, BN]> {
    const bump = new BN(0);

    while (bump.toNumber() < 255) {
        try {
            const vaultOwner = await PublicKey.createProgramAddress(
                [market.toBuffer(), bump.toArrayLike(Buffer, "le", 8)],
                dexProgramId
            );

            return [vaultOwner, bump];
        } catch (_e) {
            bump.iaddn(1);
        }
    }

    throw new Error("no seed found for vault owner");
}

export function toPublicKeys(
    obj: Record<string, string | PublicKey | HasPublicKey | any>
): any {
    const newObj = {};

    for (const key in obj) {
        const value = obj[key];

        if (typeof value == "string") {
            newObj[key] = new PublicKey(value);
        } else if (typeof value == "object" && "publicKey" in value) {
            newObj[key] = value.publicKey;
        } else {
            newObj[key] = value;
        }
    }

    return newObj;
}

interface HasPublicKey {
    publicKey: PublicKey;
}

export async function main() {
    const authority = Keypair.fromSecretKey(
        Uint8Array.from(
            JSON.parse(
                fs.readFileSync('/home/galactus/.config/solana/id.json', 'utf-8'),
            ),
        ),
    );
    const connection = new web3.Connection("http://ams43.rpcpool.com/e799f07636220ffd01dff51604bf");
    const dex_id = new PublicKey("srmqPvymJeFKQ4zGQed1GFppgkRHL9kaELCbyksJtPX");
    const sol = new PublicKey("So11111111111111111111111111111111111111112");
    const usdt = new PublicKey("Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB");
    const msol = new PublicKey("mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So");
    const wheEth = new PublicKey("7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs");
    const usdc = new PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v");

    console.log('deploying solana');
    const solMarket = await createMarket(
        connection,
        authority,
        dex_id,
        {
            baseToken: sol,
            quoteToken: usdc,
            baseLotSize: 1000000,
            quoteLotSize: 1,
            feeRateBps: 0,
        }, 1048588);

    console.log('deploying usdt');
    const usdtMarket = await createMarket(
            connection,
            authority,
            dex_id,
            {
                baseToken: usdt,
                quoteToken: usdc,
                baseLotSize: 1000000,
                quoteLotSize: 100,
                feeRateBps: 0,
            }, 1048588);
    
    console.log('deploying msol'); 
    const msolMarket = await createMarket(
        connection,
        authority,
        dex_id,
        {
            baseToken: msol,
            quoteToken: usdc,
            baseLotSize: 1000000,
            quoteLotSize: 1,
            feeRateBps: 0,
        }, 1048588);

    console.log('deploying eth');
    const ethMarket = await createMarket(
        connection,
        authority,
        dex_id,
        {
            baseToken: wheEth,
            quoteToken: usdc,
            baseLotSize: 10000,
            quoteLotSize: 100,
            feeRateBps: 0,
        }, 1048588);

    //console.log(solMarket.address.toString);
    console.log(usdtMarket.address.toString);
    console.log(msolMarket.address.toString);
    console.log(ethMarket.address.toString);
}

main().then(x => {
    console.log('finished sucessfully')
}).catch(e => {
    console.log('caught an error : ' + e)
})

