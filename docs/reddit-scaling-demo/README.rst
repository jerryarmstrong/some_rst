README.md
=========

Last edited: 2020-08-26 08:56:56

Contents:

.. code-block:: md

    <p align="center">
  <a href="https://solana.com">
    <img alt="Solana" src="https://i.imgur.com/OMnvVEz.png" width="250" />
  </a>
</p>

# Reddit Demo

Source for Solana Reddit demo, which uses the solana token program to run the Reddit benchmark challenge.
This is a fork of the solana-program-library repo.

## Build the token program

These programs cannot be built directly via cargo and instead require the build scripts located in Solana's BPF-SDK.

Download or update the BPF-SDK by running:
```bash
$ ./do.sh update
```

Build the token program:
```bash
$ ./do.sh build <program>
```

## Running the token demo

Set the RPC_URL environment variable to point to the cluster desired:

```bash
export RPC_URL=https://testnet.solana.com
export RPC_URL=https://api.mainnet-beta.solana.com
```

You'll need npm installed, then perform the following:

```bash
$ cd token/js
$ npm install
$ npm run bench -- --num_accounts 1 --num_transfer 1 --num_burn 1 --num_mint 1 --payer_account payer.json --id 0 --num_payers 4
```

That should print a message like:
> Loading payer account from payer.json
> loaded 9Rd5aWW84WtnM2QznNHqN1FmtEyb6hUf4eewp9BFBvE1

If the network you are running on doesn't have a faucet, then fund that key with some sol, then run the program again,
adjusting the arguments to the desired accounts/tranfers to generate:
```bash
$ npm run bench -- --num_accounts 10 --num_transfer 1000 --num_burn 1000 --num_mint 10 --payer_account payer.json --id 0 --num_payers 4
```

To run more than one instance, there is another script run.sh:

```bash
./run.sh <number-of-instances>
```

That will run a number of demo programs in parallel.


