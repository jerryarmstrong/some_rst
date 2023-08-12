token/js/bench/main.js
======================

Last edited: 2020-08-26 08:56:56

Contents:

.. code-block:: js

    /**
 * Reddit bench program
 *
 * Reqs:
 * 100,000 point claims
 * 75,000 burns
 * 25,000 subscriptions
 * 100,000 transfers
 *
 * @flow
 */

import {
  loadTokenProgram,
  createMint,
  createAccounts,
  token_transfer,
  approveRevoke,
  invalidApprove,
  failOnApproveOverspend,
  setOwner,
  mintTo,
  multisig,
  burn,
  closeAccount,
  nativeToken,
  getConnection,
} from './token-test';
import {Store} from '../client/util/store';
import {Account, SystemProgram, TransferParams} from '@solana/web3.js';
import {newAccountWithLamports} from '../client/util/new-account-with-lamports';
import {sendAndConfirmTransaction} from '../client/util/send-and-confirm-transaction';
import mkdirp from 'mkdirp-promise';
const {argv} = require('yargs')
  .require("num_accounts")
  .require("num_transfer")
  .require("num_burn")
  .require("num_mint")
  .require("payer_account")
  .require("id")
  .require("num_payers")

const fs = require('fs');

async function main() {
  await mkdirp("accounts");
  console.log("Making connection");
  const connection = await getConnection();
  console.log("done.");

  if (argv.create_payer) {
    var payer_account = new Account();
    fs.writeFileSync(argv.payer_account, payer_account.secretKey);
    console.log("Wrote " + payer_account.publicKey + " to " + argv.payer_account);
    return;
  }

  var payer: Account;
  var payer_balance;
  try {
    console.log("Loading payer account from " + argv.payer_account);
    var payer_buffer = fs.readFileSync(argv.payer_account);
    payer = new Account(Uint8Array.from(payer_buffer));
    console.log("loaded " + payer.publicKey);
    const info = await connection.getAccountInfo(payer.publicKey);
    console.log("  using payer with " + info.lamports + " lamports.");
    payer_balance = info.lamports;
  } catch (err) {
    console.log("Payer account doesn't exist. " + err);
    var payer_account = await newAccountWithLamports(connection, 100000000000);
    const backup_id = Math.ceil(Math.random() * 10000);
    try {
      fs.copyFile(argv.payer_account, "payer_backup" + backup_id + ".json");
    } catch (e) {
      console.log("error backing up file:" + e);
    }
    fs.writeFileSync(argv.payer_account, payer_account.secretKey);
    payer = payer_account;
    const info = await connection.getAccountInfo(payer.publicKey);
    console.log("  using payer with " + info.lamports + " lamports.");
    payer_balance = info.lamports;
  }

  var start = Date.now();
  console.log('Starting reddit test: loading token program..');
  await loadTokenProgram(connection, payer, argv.v);
  const load_token_time = (Date.now() - start);
  console.log("loaded in " + load_token_time + " ms");

  console.log('Creating reddit token mint account..');
  start = Date.now();
  var mintAmount = argv.num_accounts * argv.num_transfer * 10;
  var mintOwner = await createMint(connection, payer, argv.id, mintAmount, argv.v);
  const mint_create_time = (Date.now() - start);
  console.log("  mint created in " + mint_create_time + " ms");

  const blockhash = await connection.getRecentBlockhashAndContext();
  //console.dir(blockhash);
  const perSig = blockhash.value.feeCalculator.lamportsPerSignature;
  if (argv.v) {
    console.log("fees: " + perSig);
  }
  var totalFees = 2 * perSig * (argv.num_transfer + (2 * argv.num_accounts) + argv.num_mint + argv.num_burn);
  if (argv.v) {
    console.log("total fees: " + totalFees);
  }
  var feesPerPayer = Math.ceil(totalFees / argv.num_payers);
  console.log("funding " + argv.num_payers + " with " + feesPerPayer + " fees.");
  var payers = [];
  for (var i = 0; i < argv.num_payers; i++) {
    var new_payer = new Account();
    fs.writeFileSync("accounts/payer_" + i + "_" + argv.id + ".json", new_payer.secretKey);
    var params: TransferParams = {
      fromPubkey: payer.publicKey,
      toPubkey: new_payer.publicKey,
      lamports: feesPerPayer,
    };
    var tx = SystemProgram.transfer(params);
    var success = false;
    for (var j = 0; j < 10; j++) {
      try {
        await sendAndConfirmTransaction('fund payers', connection, tx, payer);
        payers.push(new_payer);
        break;
      } catch(e) {
        console.log("fund payers failed: " + e);
      }
    }
  }

  console.log('Creating subreddit accounts.. ' + argv.num_accounts);
  start = Date.now();
  var [accounts, owners] = await createAccounts(argv.num_accounts, argv.id, argv.v);
  const create_time = (Date.now() - start);
  console.log("  accounts created in " + create_time + " ms");

  console.log('Starting transfers ' + argv.num_transfer);
  start = Date.now();
  await token_transfer(argv.num_transfer, accounts, owners, payers, (mintAmount / argv.num_accounts), argv.v);
  const transfer_time = (Date.now() - start);
  console.log("  transfers took " + transfer_time + " ms");

  console.log('Minting ' + argv.num_mint + " to " + argv.num_accounts + " accounts.");
  start = Date.now();
  await mintTo(accounts, argv.num_mint);
  const mint_time = (Date.now() - start);
  console.log("  minting took " + mint_time + " ms");

  console.log('Burning subreddit tokens.. ' + argv.num_burn);
  start = Date.now();
  await burn(accounts, owners, argv.num_burn, payers);
  const burn_time = (Date.now() - start);
  console.log("  burn took " + burn_time + " ms");

  for (var i = 0; i < payers.length; i++) {
    const info = await connection.getAccountInfo(payers[i].publicKey);
    console.log("  payer " + i + " now has " + info.lamports + " lamports.");

    var params: TransferParams = {
      fromPubkey: payers[i].publicKey,
      toPubkey: payer.publicKey,
      lamports: info.lamports - (2 * perSig),
    };

    var tx = SystemProgram.transfer(params);
    try {
      await sendAndConfirmTransaction('defund payers', connection, tx, payers[i]).catch(e => {});
    } catch (e) {
      console.log("defund payers failed with: " + e);
    }
  }

  const info = await connection.getAccountInfo(payer.publicKey);
  console.log("  payer now has " + info.lamports + " lamports. Took " + (payer_balance - info.lamports));

  console.log("Summary:");
  console.log(" loaded token program in " + load_token_time + " ms");
  console.log(" minting account created in " + mint_create_time + " ms");
  console.log(" created " + argv.num_accounts + " accounts in " + create_time + " ms");
  console.log(" " + argv.num_transfer + " transfers in " + transfer_time + " ms");
  console.log(" " + argv.num_mint + " token mints in " + mint_time + " ms");
  console.log(" " + argv.num_burn + " token burns in " + burn_time + " ms");
  const total = load_token_time + mint_create_time + create_time + transfer_time + mint_time + burn_time;
  console.log(" total: " + total + " ms");
  console.log('Success\n');
}

main()
  .catch(err => {
    console.error(err);
    process.exit(-1);
  })
  .then(() => process.exit());


