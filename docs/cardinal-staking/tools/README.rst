tools/README.md
===============

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: md

    # How To Use

## Setup

All scripts can be run via `cli`

```
git clone https://github.com/cardinal-labs/cardinal-staking
cd cardinal-staking
yarn
```

## Getting Started

All scripts can be run via `cli`. Run the command to view the tools enabled on the cli and read their description.

```
ts-node tools/cli.ts
```

The CLI is configured with environment variables and can be set by creating a `.env` file in the same directory as the repo.

# Example Scripts

## checkMultiplier.ts

### Params

`cluster`, `rewardDistributorId`

### Usage:

Used to check the multipliers of all the reward entries corresponding to the given reward distibutor

## checkStakeEntry.ts

### Params:

`cluster`, `stakePoolId`, `mintId`

### Usage:

Used to look up and log the stake entry and reward entry for a given mint

## closePools.ts

### Params:

`cluster`, `poolIds`

### Usage:

Used to **safely** close a pool by making sure there are not staked tokens in the pool, closing all stake and reward entries, then closing the reward distributor and then closing the pool. All fund associated with closing the accounts are directed to the `wallet` which is initiating the close.

### Constraint

`wallet` has to match the pool authority for the script to run successfully

## createFungibleToken.ts

### Params:

`cluster`, `mintKeypair`

### Usage:

Handy script to create a fungible token with configurable `SUPPLY` and `DECIMALS`

## getMetadataForPoolTokens

### Params:

`poolId`, `metadataKeys`

### Usage:

Given a list of metadata keys and a pool pubkey, the script looks up all staked tokens for the given pool and logs the metadata requested from `metadataKeys` array for every staked mint.

## initializeEntriesAndSetMultipliers.ts

### Params:

`stakePoolId`, `entries`, `cluster`, `fungible`

### Usage:

Given `MINT_LIST`, a list of entries in the format

```
{
    mintId: new PublicKey("MINT_ID"),
    multiplier: 200,
  },
```

the script is used to initialize stake entries and reward entries for a given stake pool. The script allows the functionality of providing **custom multipliers** for given mints, so it can also be used to set multipliers for given mints.

## reclaimFunds.ts

### Params:

`stakePoolId`, `amount`, `cluster`

### Usage:

Reclaims `amount` numerb of tokens from the reward distributor associated with the pool provided.

### Constraint

Only the stake pool authority can successfully execute this transaction

## updateMultipliersOnRules.ts

### Params:

`UPDATE_RULES`, `stakePoolId`, `cluster`

### Usage:

Given `UPDATE_RULES`, the script is used to update the multipliers of reward entries according to give rules specified in the script. Rules option can be `volume` (if user stakes 2+ token, set token multpliers to `X`, if user staked 5+ token, set token multiplier to `Y`), `metadata` (if token has metadata attribute equal to specify value, set `X` multiplier), and `combination` (if user has to stake A,B,C mints together, token get `X` multiplier, else set to zero). Rules can only be set by the pool authority.


