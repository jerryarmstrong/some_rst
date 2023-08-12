index.ts
========

Last edited: 2023-03-27 09:30:13

Contents:

.. code-block:: ts

    import { MangoUtils } from "./utils/mango_utils";
import { Connection, Keypair, LAMPORTS_PER_SOL, PublicKey } from '@solana/web3.js';
import { sleep, Cluster } from "@blockworks-foundation/mango-client";
import { getProgramMap } from "./utils/config"
import * as fs from 'fs';

export async function main() {
    
    // cluster should be in 'devnet' | 'mainnet' | 'localnet' | 'testnet'  
    const cluster = (process.env.CLUSTER || 'localnet') as Cluster;

    const programNameToId = getProgramMap(cluster);
    const endpoint = process.env.ENDPOINT_URL || 'http://0.0.0.0:8899';
    const connection = new Connection(endpoint, 'confirmed');
    console.log('Connecting to cluster ' + endpoint)
    if (!fs.existsSync('authority.json')) {
        //create an authority.json
        const new_authority = Keypair.generate();
        fs.writeFileSync('authority.json', '[' + new_authority.secretKey.toString() + ']');
    }
    const authority = Keypair.fromSecretKey(
        Uint8Array.from(
          JSON.parse(
            process.env.KEYPAIR ||
              fs.readFileSync('authority.json', 'utf-8'),
          ),
        ),
      );
    const do_log_str = process.env.LOG || "false";
    const do_log = do_log_str === "true";

    console.log('Configuring authority')
    const balance = await connection.getBalance(authority.publicKey)
    if (balance < 100) {
        const signature = await connection.requestAirdrop(authority.publicKey, LAMPORTS_PER_SOL * 100);
        await connection.confirmTransaction(signature, 'confirmed');
    }
    const beginSlot = await connection.getSlot();
    console.log('Creating Mango Cookie')
    const mangoProgramId = new PublicKey(programNameToId['mango'])
    const dexProgramId = new PublicKey(programNameToId['serum_dex']);
    const pythProgramId = new PublicKey(programNameToId['pyth_mock']);

    let logId = 0
    if (do_log) {
        logId = connection.onLogs(mangoProgramId, (log, ctx) => {
            if (log.err != null) {
                console.log("mango error : ", log.err)
            }
            else {
                for (const l of log.logs) {
                    console.log("mango log : " + l)
                }
            }
        });
    }

    try {
        const mangoUtils = new MangoUtils(connection, authority, mangoProgramId, dexProgramId, pythProgramId);

        const cookie = await mangoUtils.createMangoCookie(['MNGO', 'SOL', 'BTC', 'ETH', 'AVAX', 'SRM', 'FTT', 'RAY', 'MNGO', 'BNB', 'GMT', 'ADA'])

        console.log('Creating ids.json');
        const json = mangoUtils.convertCookie2Json(cookie, cluster)
        fs.writeFileSync('ids.json', JSON.stringify(json, null, 2));
        fs.writeFileSync('authority.json', '[' + authority.secretKey.toString() + ']');
        console.log('Mango cookie created successfully')

        const nbUsers = Number(process.env.NB_USERS || "1");
        console.log('Creating ' + nbUsers + ' Users');
        const users = (await mangoUtils.createAndMintUsers(cookie, nbUsers, authority)).map(x => {
            const info = {};
            info['publicKey'] = x.kp.publicKey.toBase58();
            info['secretKey'] = Array.from(x.kp.secretKey);
            info['mangoAccountPks'] = [x.mangoAddress.toBase58()];
            return info;
        })
        console.log('created ' + nbUsers + ' Users');
        fs.writeFileSync('accounts.json', JSON.stringify(users));

    } finally {
        if (logId) {
            // to log mango logs
            await sleep(5000)
            const endSlot = await connection.getSlot();
            const blockSlots = await connection.getBlocks(beginSlot, endSlot);
            console.log("\n\n===============================================")
            for (let blockSlot of blockSlots) {
                const block = await connection.getBlock(blockSlot);
                for (let i = 0; i < block.transactions.length; ++i) {
                    if (block.transactions[i].meta.logMessages) {
                        for (const msg of block.transactions[i].meta.logMessages) {
                            console.log('solana_message : ' + msg);
                        }
                    }
                }
            }

            connection.removeOnLogsListener(logId);
        }
    }
}

main().then(x => {
    console.log('finished sucessfully')
}).catch(e => {
    console.log('caught an error : ' + e)
})


