token/js/bench/token-test.js
============================

Last edited: 2020-08-26 08:56:56

Contents:

.. code-block:: js

    // @flow

import fs from 'mz/fs';
import {Account, Connection, BpfLoader, PublicKey} from '@solana/web3.js';
import semver from 'semver';

import {Token, TokenAmount} from '../client/token';
import {url} from '../url';
import {newAccountWithLamports} from '../client/util/new-account-with-lamports';
import {sleep} from '../client/util/sleep';
import {Store} from '../client/util/store';

// Loaded token program's program id
let programId: PublicKey;

// A token created by the next test and used by all subsequent tests
let mintOwner: Account;
let testToken: Token;

// Initial token account
let testAccountOwner: Account;
let testAccount: PublicKey;

function assert(condition, message) {
  if (!condition) {
    console.log(Error().stack + ':token-test.js');
    throw message || 'Assertion failed';
  }
}

async function didThrow(func, args): Promise<boolean> {
  try {
    await func.apply(args);
  } catch (e) {
    return true;
  }
  return false;
}

let connection;
export async function getConnection(): Promise<Connection> {
  if (connection) return connection;

  let newConnection = new Connection(url, 'recent', );
  console.log("get version");
  var version = null;
  for (var i = 0; i < 20; i++) {
    try {
      version = await newConnection.getVersion();
      break;
    } catch (e) {
      console.log("error: " + e);
      await sleep(200);
    }
  }
  console.log("done");

  // commitment params are only supported >= 0.21.0
  const solanaCoreVersion = version['solana-core'].split(' ')[0];
  if (semver.gte(solanaCoreVersion, '0.21.0')) {
    newConnection = new Connection(url, 'recent');
  }

  // eslint-disable-next-line require-atomic-updates
  connection = newConnection;
  console.log('Connection to cluster established:', url, version);
  return connection;
}

async function loadProgram(connection: Connection, payer, path: string): Promise<PublicKey> {
  const NUM_RETRIES = 500; /* allow some number of retries */
  const data = await fs.readFile(path
  );
  const { feeCalculator } = await connection.getRecentBlockhash();
  const balanceNeeded =
    feeCalculator.lamportsPerSignature *
    (BpfLoader.getMinNumSignatures(data.length) + NUM_RETRIES) +
    (await connection.getMinimumBalanceForRentExemption(data.length));

  const program_account = new Account();
  console.log('Loading program:', path);
  for (var i = 0; i < 10; i++) {
    try {
      await BpfLoader.load(connection, payer, program_account, data);
      break;
    } catch (e) {
    }
  }
  console.log("done");
  return program_account.publicKey;
}

async function GetPrograms(connection: Connection, payer: Account, verbose: boolean = false): Promise<PublicKey> {
  const store = new Store();
  let tokenProgramId = null;
  try {
    const config = await store.load('config.json');
    console.log('Using pre-loaded Token program');
    console.log('  Note: To reload program remove client/util/store/config.json');
    tokenProgramId = new PublicKey(config.tokenProgramId);
    console.log("Checking that account exists..");
    const info = await connection.getAccountInfo(tokenProgramId);
    if (verbose) {
      console.log(".. got account info: ");
      console.dir(info);
    }
    if (info === null) {
      console.log("account doesn't exist..creating new");
      throw new Error('failed to find account');
    }
  } catch (err) {
    tokenProgramId = await loadProgram(connection, payer, '../target/bpfel-unknown-unknown/release/spl_token.so');
    await store.save('config.json', {
      tokenProgramId: tokenProgramId.toString(),
    });
  }
  return tokenProgramId;
}

export async function loadTokenProgram(connection, payer): Promise<void> {
  programId = await GetPrograms(connection, payer);

  console.log('Token Program ID', programId.toString());
}

export async function loadOrCreateAccount(file, connection, verbose: boolean = false): Account {
  var account: Account;
  try {
    if (verbose) {
      console.log("Loading account from " + file);
    }
    var buffer = fs.readFileSync(file);
    account = new Account(Uint8Array.from(buffer));
    if (verbose) {
      console.log("loaded " + account.publicKey);
    }
    /*const info = await connection.getAccountInfo(account.publicKey);
    if (info) {
      console.log("  using account with " + info.lamports + " lamports.");
    } else {
      console.log("  account not loaded yet.");
    }*/
  } catch (err) {
    if (verbose) {
      console.log("account doesn't exist. " + err);
    }
    var account = new Account();
    fs.writeFileSync(file, account.secretKey);
    /*const info = await connection.getAccountInfo(account.publicKey);
    console.dir(info);
    if (info) {
      console.log("  using payer with " + info.lamports + " lamports.");
    } else {
      console.log("  account not loaded yet.");
    }*/
  }

  return account;
}

export async function createMint(connection, payer, id, amount, verbose): Promise<Account> {
  mintOwner = await loadOrCreateAccount("accounts/mint_owner_" + id + ".json", connection);
  var mintAccount = await loadOrCreateAccount("accounts/mint_" + id + ".json", connection);
  testAccountOwner = await loadOrCreateAccount("accounts/test_owner_" + id + ".json", connection);
  var initialTokenAccount = await loadOrCreateAccount("accounts/first_token_account_" + id + ".json", connection);
  console.log("creating mint..");
  [testToken, testAccount] = await Token.createMint(
    connection,
    payer,
    mintAccount,
    mintOwner.publicKey,
    testAccountOwner.publicKey,
    initialTokenAccount,
    new TokenAmount(amount),
    2,
    programId,
    true,
  );
  console.log("done.");

  const mintInfo = await testToken.getMintInfo();
  if (verbose) {
    console.dir(mintInfo);
  }
  assert(mintInfo.decimals == 2);
  //assert(mintInfo.owner == null);

  const accountInfo = await testToken.getAccountInfo(testAccount);
  assert(accountInfo.mint.equals(testToken.publicKey));
  assert(accountInfo.owner.equals(testAccountOwner.publicKey));
  if (accountInfo.amount.toNumber() < amount) {
    console.log("minting to testToken");
    await testToken.mintTo(testAccount, mintOwner, [], amount);
  }
  console.log("mint amount: " + accountInfo.amount.toNumber());
  //assert(accountInfo.amount.toNumber() == amount);
  assert(accountInfo.delegate == null);
  assert(accountInfo.delegatedAmount.toNumber() == 0);
}

export async function createAccounts(numAccounts, id, verbose): Promise<void> {
  const balanceNeeded = await Token.getMinBalanceRentForExemptAccount(
    connection,
  );
  console.log("balance needed: " + balanceNeeded);

  var destOwners = [];
  var num_success = 0;
  const chunkSize = 10;
  var numChunks = numAccounts / chunkSize;
  var total = 0;
  var accounts = [];
  for (var i = 0; i < numChunks; i++) {
    var create_promises = [];
    for (var j = 0; j < chunkSize; j++) {
      if (total >= numAccounts) {
        break;
      }
      total += 1;
      const destOwner = await loadOrCreateAccount("accounts/account_owner_" + id + "_" + total + ".json", connection);
      const newAccount = await loadOrCreateAccount("accounts/account_" + id + "_" + total + ".json", connection);
      create_promises.push(
        testToken.createAccount(destOwner.publicKey, newAccount, balanceNeeded / 8)
        .then((account) => {
          num_success += 1;
          return account;
        })
        .catch(e => {
          console.log("error: ", e);
        })
      );
      destOwners.push(destOwner);
    }

    var new_accounts = await Promise.all(create_promises);
    accounts.push(...new_accounts);
    console.log("created: " + num_success);
  }

  assert(accounts.length > 0);
  for (var i = 0; i < accounts.length; i++) {
    let account = accounts[i];
    let destOwner = destOwners[i];
    if (verbose) {
      console.log("Getting info for " + account);
    }
    const accountInfo = await testToken.getAccountInfo(account);
    assert(accountInfo.mint.equals(testToken.publicKey));
    assert(accountInfo.owner.equals(destOwner.publicKey));
    if (verbose) {
      console.log(account + " has " + accountInfo.amount);
    }
    //assert(accountInfo.amount.toNumber() == 0);
    assert(accountInfo.delegate == null);
  }
  return [accounts, destOwners];
}

// 100,000 transfers
export async function token_transfer(numTransfer, accounts, owners, payers, amount, verbose): Promise<void> {
  if (verbose) {
    console.log("accounts: " + accounts.length);
  }
  var dests = new Map();
  var num_success = 0;
  var num_error = 0;
  const accountInfo = await testToken.getAccountInfo(testAccount);
  //console.log("account info: ");
  //console.dir(accountInfo);
  if (accountInfo.amount.toNumber() < numTransfer * amount) {
    assert("not enough tokens!");
  }
  var chunkSize = 10;
  var numChunks = accounts.length / chunkSize;
  var total = 0;

  for (var i = 0; i < accounts.length; i++) {
    let initial_balance = await testToken.getAccountInfo(accounts[i]);
    if (initial_balance) {
      dests.set(accounts[i], initial_balance.amount.toNumber());
    }
  }

  // Fund accounts from mint
  var start = Date.now();
  for (var i = 0; i < numChunks; i++) {
    var transfer_promises = [];
    for (var j = 0; j < chunkSize; j++) {
      if (total >= accounts.length) {
        break;
      }
      total += 1;
      const dest = accounts[total % accounts.length];
      //console.log("transfer to " + dest);
      const payer = payers[total % payers.length];
      transfer_promises.push(testToken.transfer(testAccount, dest, testAccountOwner, [], amount, payer)
        .then(() => {
          num_success += 1;
        })
        .catch(e => {
            console.log(dest + " error: " + e + " " + dests.get(dest));
            dests.set(dest, dests.get(dest) - amount);
            num_error += 1;
        })
      );
      if (dests.has(dest)) {
        dests.set(dest, dests.get(dest) + amount);
      } else {
        dests.set(dest, amount);
      }
    }

    await Promise.all(transfer_promises);
    if ((Date.now() - start) > 2000) {
      console.log("transfers: num_success: " + num_success + " error: " + num_error);
      start = Date.now();
    }
  }

  const NUM_POLL = 10;
  for (var i = 0; i < NUM_POLL; i++) {
    for (let [dest, amount] of dests) {
      let destAccountInfo = await testToken.getAccountInfo(dest);
      if (verbose) {
        console.log(dest + " has " + destAccountInfo.amount + " expected: " + amount);
      }
      if (destAccountInfo.amount.toNumber() === amount) {
        dests.delete(dest);
      }
    }

    if (verbose) {
      console.log("accounts left: " + dests.size);
    }
    if (dests.size == 0) {
      break;
    }
    //assert(destAccountInfo.amount.toNumber() == 1);
    await sleep(200);
  }
  assert(dests.size == 0);

  console.log("starting inter-account transfers " + accounts.length);
  // Do some transfers between accounts.
  num_success = 0;
  num_error = 0;
  if (accounts.length > 2) {
    var chunkSize = 10;
    var numChunks = numTransfer / chunkSize;
    var total = 0;
    var start = Date.now();
    for (var i = 0; i < numChunks; i++) {
      var transfer_promises = [];
      for (var j = 0; j < chunkSize; j++) {
        if (total >= numTransfer) {
          break;
        }
        const payer = payers[total % payers.length];
        const src_idx = (total * 2) % accounts.length;
        const dst_idx = (total * 2 + 1) % accounts.length;
        const src = accounts[src_idx];
        const srcOwner = owners[src_idx];
        const dest = accounts[dst_idx];
        //console.log("transferring " + src_idx + " to " + dst_idx);
        total += 1;
        transfer_promises.push(
          testToken.transfer(src, dest, srcOwner, [], 1, payer)
            .then((x) => {
              num_success += 1;
            })
            .catch(e => {
              num_error += 1;
              console.log("transfer error: " + e);
            })
        );
      }
      if ((Date.now() - start) > 10000) {
        console.log("transfers: num_success: " + num_success + " error: " + num_error);
        start = Date.now();
      }
      await Promise.all(transfer_promises);
    }
  }
  console.log("done.. success: " + num_success + " error: " + num_error);
}

// 100,000 mint
export async function mintTo(accounts, num_mint): Promise<void> {
  const connection = await getConnection();

  var num_success = 0;
  var num_error = 0;
  const chunkSize = 10;
  const numChunks = num_mint / chunkSize;
  var total = 0;
  var start = Date.now();
  for (var i = 0; i < numChunks; i++) {
    var mint_promises = [];
    for (var j = 0; j < chunkSize; j++) {
      if (total > num_mint) {
        break;
      }
      total += 1;
      var dest = accounts[total % accounts.length];
      mint_promises.push(
        testToken.mintTo(dest, mintOwner, [], 42)
        .then(() => { num_success += 1; })
        .catch(e => {
          console.log("  " + dest + " mint error: " + e);
          num_error += 1;
        })
      );
    }

    await Promise.all(mint_promises);
    if ((Date.now() - start) > 10000) {
      console.log("  mint success: " + num_success + " error: " + num_error + " " + (Date.now() - start) + " ms");
      start = Date.now();
    }
  }
}

// 75,000 burns
export async function burn(accounts, owners, numBurn, payers): Promise<void> {
  var burnPromises = [];
  var chunkSize = 10;
  var numChunks = numBurn / chunkSize;
  var numBurned = 0;
  var num_success = 0;
  var num_fail = 0;
  var total = 0;
  var start = Date.now();
  for (var i = 0; i < numChunks; i++) {
    for (var j = 0; j < chunkSize; j++) {
      if (total >= numBurn) {
        break;
      }
      total += 1;
      var dest = accounts[total % accounts.length];
      var destOwner = owners[total % accounts.length];
      var payer = payers[total % payers.length];

      numBurned += 1;
      burnPromises.push(
        testToken.burn(dest, destOwner, [], 1, payer)
          .then((account) => {
            num_success += 1;
          })
        .catch(e => {
          console.log("burn error: " + e);
          num_fail += 1;
        }));
    }
    await Promise.all(burnPromises);
    if ((Date.now() - start) > 2000) {
      console.log("burned " + numBurned + " success: " + num_success + " num_fail: " + num_fail + " " + (Date.now() - start) + " ms");
      start = Date.now();
    }
  }

  console.log("Done burning.");
  /*for (var j = 0; j < 100; j++) {
    accountInfo = await testToken.getAccountInfo(testAccount);
    if (accountInfo.amount.toNumber() == amount - 1) {
      break;
    }
    await sleep(100);
  }*/
}



